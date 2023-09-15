from django.utils import timezone
from django.db import models
from django.db.models import Sum
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from ckeditor.fields import RichTextField

from apps.common.models import BaseModel
from apps.users.models import Profile

class HappeningBaseModel(models.Model):
    created_at = models.DateTimeField(_("Created time"), auto_now_add=True)
    updated_at = models.DateTimeField(_("Modified time"), auto_now=True)

    cover_image = models.ImageField(_("Cover image"), upload_to="happenings/cover/")
    title = models.CharField(_("Title"), max_length=100)
    slug = models.SlugField(_("Slug"), max_length=100)

    class Meta:
        abstract = True


class Tag(BaseModel):
    name = models.CharField(_("Name"), max_length=50)

    class Meta:
        verbose_name = _("Tag")
        verbose_name_plural = _("Tags")

    def __str__(self) -> str:
        return self.name


class News(HappeningBaseModel):
    body = RichTextField(_("Body"), max_length=1000)
    is_active = models.BooleanField(_("Is active"), default=False)
    tags = models.ManyToManyField(Tag, related_name="news", verbose_name=_("Tags"))

    class Meta:
        verbose_name = _("News")
        verbose_name_plural = _("News")
        ordering = ["-is_active", "-updated_at"]

    def __str__(self) -> str:
        return self.title


class Poll(HappeningBaseModel):
    is_active = models.BooleanField(_("Is active"), default=False)

    class Meta:
        verbose_name = _("Poll")
        verbose_name_plural = _("Polls")

    def get_total_votes(self):
        votes = self.choices.aggregate(Sum("votes"))["votes__sum"]
        return votes if votes else 0

    def __str__(self):
        return self.title


class PollChoice(BaseModel):
    text = models.CharField(_("Text"), max_length=100)
    votes = models.PositiveIntegerField(_("Votes"), default=0)
    order = models.PositiveSmallIntegerField(_("Order"), default=0)
    poll = models.ForeignKey(
        Poll,
        related_name="choices",
        on_delete=models.CASCADE,
        verbose_name=_("Poll")
    )

    class Meta:
        verbose_name = _("Poll choice")
        verbose_name_plural = _("Poll choices")
        ordering = ["order"]

    def __str__(self):
        return self.text


class UserPoll(BaseModel):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="polls", verbose_name=_("Profile"))
    choice = models.ForeignKey(
        PollChoice, on_delete=models.CASCADE, related_name="users_choices", verbose_name="Choice"
    )

    class Meta:
        verbose_name = _("User Poll Choice")
        verbose_name_plural = _("User Poll Choices")
        unique_together = ["profile", "choice"]

    def __str__(self):
        return f"{self.profile.__str__()}: {self.choice.__str__()}"


class Event(HappeningBaseModel):
    location = models.CharField(_("Location"), max_length=100)
    time = models.DateTimeField(_("Time"))
    about = RichTextField(_("About"), max_length=1000)

    class Meta:
        verbose_name = _("Event")
        verbose_name_plural = _("Events")
        ordering = ["-time"]

    def clean(self):
        if self.time < timezone.now():
            raise ValidationError(_("This datetime must be greater than or equal to current time."))

    def __str__(self):
        return self.title
