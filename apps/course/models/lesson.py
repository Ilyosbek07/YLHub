from ckeditor_uploader.fields import RichTextUploadingField

from apps.common.models import BaseModel
from django.db import models
from django.utils.translation import gettext as _

from apps.course.models.cource import Course
from apps.users.models import Profile


class LessonTypeChoices(models.TextChoices):
    VIDEO = "video", _("Video")
    TASK = "task", _("Task")
    EXAM = "exam", _("Exam")
    BOOK = "book", _("Book")
    AUDIOBOOK = "audiobook", _("Audio book")


class Lesson(BaseModel):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name=_("Course"))
    title = models.CharField(max_length=125, verbose_name=_("Title"))
    description = models.TextField(verbose_name=_("Description"))
    type = models.CharField(max_length=55, choices=LessonTypeChoices.choices, verbose_name=_("Type"))
    order = models.IntegerField(verbose_name=_("Order"))
    points = models.IntegerField(verbose_name=_("Points"))

    class Meta:
        verbose_name = _("Lesson")
        verbose_name_plural = _("Lessons")

    def __str__(self):
        return self.title


class LessonMedia(BaseModel):
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, verbose_name=_("Lesson"))
    title = models.CharField(max_length=125, verbose_name=_("Title"))
    file = models.FileField(upload_to="media/", verbose_name=_("File"))
    content = RichTextUploadingField(verbose_name='Content', null=True, blank=True)
    order = models.IntegerField(verbose_name=_("Order"))

    class Meta:
        verbose_name = _("Lesson Media")
        verbose_name_plural = _("Lesson Media")

    def __str__(self):
        return self.title


class LessonProgress(BaseModel):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, verbose_name=_("Profile"))
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, verbose_name=_("Lesson"))
    is_finish = models.BooleanField(default=False, verbose_name=_("Is Finish"))

    class Meta:
        unique_together = ['profile', 'lesson']
        verbose_name = _("Lesson Progress")
        verbose_name_plural = _("Lesson Progress")

    def __str__(self):
        return f"Lesson Progress: {self.profile} - {self.lesson}"

