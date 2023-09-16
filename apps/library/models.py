from django.db import models
from django.db.models import Sum
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.core.validators import FileExtensionValidator
from apps.common.models import BaseModel
from apps.users.models import Profile
from .choices import LanguageChoices
from .utils import get_num_pages, get_audio_length

class BookAuthor(BaseModel):
    full_name = models.CharField(_("Full name"), max_length=100)
    birth_date = models.DateField(_("Birth date"))
    country = models.CharField(_("Country"), max_length=100)
    about = models.TextField(_("About"), max_length=1000)
    avatar = models.ImageField(_("Avatar"), upload_to="library/authors/")

    class Meta:
        verbose_name = _("Book Author")
        verbose_name_plural = _("Book Authors")

    def __str__(self):
        return self.full_name


class BookCategory(BaseModel):
    name = models.CharField(_("Name"), max_length=100)
    is_popular = models.BooleanField(_("Is popular"), default=True)
    icon = models.FileField(_("Icon"), upload_to="library/category/")

    class Meta:
        verbose_name = _("Book category")
        verbose_name_plural = _("Book categories")

    def __str__(self):
        return self.name


class BookBaseModel(models.Model):
    created_at = models.DateTimeField(_("Created time"), auto_now_add=True)
    updated_at = models.DateTimeField(_("Modified time"), auto_now=True)
    title = models.CharField(_("Title"), max_length=200)
    cover_image = models.ImageField(_("Cover image"), upload_to="library/covers/")
    publication_year = models.PositiveSmallIntegerField(_("Publication year"))
    is_required = models.BooleanField(_("Is required"), default=False)
    is_recommended = models.BooleanField(_("Is recommended"), default=False)
    description = models.TextField(_("Description"), max_length=800)
    bonus_points = models.PositiveSmallIntegerField(_("Bonus points"), default=0)
    language = models.CharField(
        _("Language"),
        max_length=2,
        choices=LanguageChoices.choices
    )

    class Meta:
        abstract = True


class Book(BookBaseModel):
    deadline = models.DateField(_("Deadline"))
    book_file = models.FileField(
        _("File"), upload_to="library/pdf_files/",
        validators=[FileExtensionValidator(allowed_extensions=["pdf"])] 
    )
    pages = models.PositiveSmallIntegerField(_("Pages"), blank=True)
    author = models.ForeignKey(
        BookAuthor,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="books",
        verbose_name=_("Author")
    )
    category = models.ForeignKey(
        BookCategory,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="books",
        verbose_name=_("Category")
    )

    class Meta:
        verbose_name = _("Book")
        verbose_name_plural = _("Books")

    def save(self):
        try:
            path = self.book_file.file.temporary_file_path()
        except:
            path = self.book_file.file
        num_pages = get_num_pages(path)
        if num_pages is None:
            raise ValidationError(_("Invalid file"))
        self.pages = num_pages
        return super().save()
    
    def __str__(self):
        return self.title
    

class UserBookProgress(BaseModel):
    profile = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        related_name="book_progresses",
        verbose_name=_("Profile")
    )
    book = models.ForeignKey(
        Book,
        on_delete = models.SET_NULL,
        null=True,
        related_name="user_progresses",
        verbose_name=_("Book")
    )
    last_page = models.PositiveSmallIntegerField(_("Last page"))

    class Meta:
        verbose_name = _("User Book Progress")
        verbose_name_plural = _("User Book Progresses")
        unique_together = ["book", "profile"]

    def __str__(self):
        return f"{self.book.__str__()} : {self.profile.__str__()}"


class AudioBook(BookBaseModel):
    duration = models.PositiveIntegerField(_("Duration"), blank=True, default=0)
    author = models.ForeignKey(
        BookAuthor,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="audiobooks",
        verbose_name=_("Author")
    )
    category = models.ForeignKey(
        BookCategory,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="audiobooks",
        verbose_name=_("Category")
    )

    class Meta:
        verbose_name = _("Audiobook")
        verbose_name_plural = _("Audiobooks")

    def __str__(self):
        return self.title
    

class AudioSection(BaseModel):
    audiobook = models.ForeignKey(
        AudioBook,
        on_delete=models.CASCADE,
        related_name="sections",
        verbose_name=_("Audiobook")
    )
    order = models.PositiveSmallIntegerField(_("Order"), default=1)
    duration = models.PositiveIntegerField(_("Duration"), blank=True, default=0)
    name = models.CharField(_("Name"), max_length=100)

    class Meta:
        verbose_name = _("Audiobook section")
        verbose_name_plural = _("Audiobook sections")
        unique_together = ["order", "audiobook"]

    def __str__(self):
        return self.name


class AudioUnit(BaseModel):
    section = models.ForeignKey(
        AudioSection,
        on_delete=models.CASCADE,
        related_name="units",
        verbose_name=_("Section")
    )
    order = models.PositiveSmallIntegerField(_("Order"), default=1)
    duration = models.PositiveSmallIntegerField(_("Duration"), blank=True)
    name = models.CharField(_("Name"), max_length=100)
    audio_file = models.FileField(
        _("File"), upload_to="library/audio_files/",
        validators=[FileExtensionValidator(allowed_extensions=["mp3"])] 
    )

    class Meta:
        verbose_name = _("Audiobook unit")
        verbose_name_plural = _("Audiobook units")
        unique_together = ["order", "section"]

    def save(self):
        old = AudioUnit.objects.filter(pk=self.id)
        if old.exists():
            path = self.audio_file.file
            new_duration = -old.first().duration
        else:
            path = self.audio_file.file.temporary_file_path()
            new_duration = 0

        duration = get_audio_length(path)
        if duration is None:
            raise ValidationError(_("Invalid file"))
        self.duration = duration
        new_duration += self.duration
        self.update_ancestor_durations(new_duration)
        return super().save()
    
    def delete(self, *args, **kwargs):
        self.update_ancestor_durations(-self.duration)
        super().delete(*args, **kwargs)

    def update_ancestor_durations(self, duration):
        self.section.duration += duration
        self.section.save()
        self.section.audiobook.duration += duration
        self.section.audiobook.save()

    def __str__(self):
        return self.name


class UserAudiobookProgress(BaseModel):
    profile = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        related_name="audiobook_progresses",
        verbose_name=_("Profile")
    )
    audiobook = models.ForeignKey(
        AudioBook,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="user_progresses",
        verbose_name=_("Audio book")
    )
    audio_unit = models.ForeignKey(
        AudioUnit,
        on_delete=models.SET_NULL,
        null=True,
        related_name="user_progresses",
        verbose_name=_("Audio unit")
    )
    listened_duration = models.PositiveSmallIntegerField(_("Listened duration"), default=0)
    duration_so_far = models.PositiveIntegerField(_("Total listened duration"), blank=True)

    class Meta:
        verbose_name = _("User audiobook progress")
        verbose_name_plural = _("User audiobook progresses")
        unique_together = ["profile", "audiobook"]

    def save(self):
        section = self.audio_unit.section
        audiobook = section.audiobook

        completed_sections_len = audiobook.sections.filter(
            order__lt=section.order
        ).aggregate(Sum("duration"))["duration__sum"]
        if completed_sections_len is None:
            completed_sections_len = 0
        
        section_completed_units_len = section.units.filter(
            order__lt=self.audio_unit.order
        ).aggregate(Sum("duration"))["duration__sum"]
        if section_completed_units_len is None:
            section_completed_units_len = 0
        
        self.audiobook = audiobook
        self.duration_so_far = completed_sections_len + section_completed_units_len + self.listened_duration
        return super().save()
    
    def __str__(self):
        return f"{self.profile.__str__()} : {self.audio_unit.section.audiobook.__str__()}"
        

class LibrarySearchHistory(BaseModel):
    keyword = models.CharField(_("Search keyword"), max_length=100)
    profile = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        related_name="library_search_history",
        verbose_name=_("Profile")
    )

    class Meta:
        verbose_name = _("Library Search History")
        verbose_name_plural = _("Library Search Histories")
        ordering = ["-updated_at"]

    def __str__(self):
        return self.keyword
