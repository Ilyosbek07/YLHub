from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from apps.common.models import BaseModel
from apps.users.models import Profile
from .choices import WebinarStatusChoices, WebinarTypeChoices, ComplaintTypeChoices

class Webinar(BaseModel):
    title = models.CharField(_("Title"), max_length=100)
    author = models.CharField(_("Author"), max_length=100)
    about = models.TextField(_("About"), max_length=400)
    cover_image = models.ImageField(_("Cover image"), upload_to="webinar/covers/", default="webinar_default.png")
    stream_url = models.CharField(_("Stream url"), max_length=200, null=True, blank=True)
    status = models.CharField(
        _("Status"),
        max_length=1,
        choices=WebinarStatusChoices.choices
    )
    webinar_type = models.CharField(
        _("Type"),
        max_length=1,
        choices=WebinarTypeChoices.choices
    )

    class Meta:
        verbose_name = _("Webinar")
        verbose_name_plural = _("Webinars")

    def clean(self):
        if self.status != WebinarStatusChoices.LIVE and self.stream_url is None:
            raise ValidationError(_("This field is required."))

    def __str__(self):
        return self.title


class Comment(BaseModel):
    text = models.TextField(_("Text"), max_length=200)
    is_active = models.BooleanField(_("Is active"), default=True)
    parent = models.ForeignKey(
        to="self",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="replies",
        verbose_name=_("Parent")
    )
    webinar = models.ForeignKey(
        Webinar,
        on_delete=models.CASCADE,
        related_name="comments",
        verbose_name=_("Webinar")
    )
    owner = models.ForeignKey(
        Profile,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="comments",
        verbose_name=_("Owner")
    )

    class Meta:
        verbose_name = _("Comment")
        verbose_name_plural = _("Comments")

    def __str__(self):
        return self.text


class CommentComplaint(BaseModel):
    description = models.TextField(_("Description"), max_length=200, null=True, blank=True)
    owner = models.ForeignKey(
        Profile,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="comment_complaints",
        verbose_name=_("Owner")
    )
    comment = models.ForeignKey(
        Comment,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="complaints",
        verbose_name=_("Comment")
    )
    complaint_type = models.CharField(
        _("Type"),
        max_length=1,
        choices=ComplaintTypeChoices.choices
    )

    class Meta:
        verbose_name = _("Comment complaint")
        verbose_name_plural = _("Comment complaints")

    def clean(self):
        if self.complaint_type == ComplaintTypeChoices.OTHER:
            if self.description is None:
                raise ValidationError(_("You have to specify your complaint in detail."))
        else:
            self.description = ""

    def __str__(self):
        return self.owner.__str__()
    

class WebinarSearchHistory(BaseModel):
    keyword = models.CharField(_("Search keyword"), max_length=100)
    profile = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        related_name="webinar_search_history",
        verbose_name=_("Profile")
    )

    class Meta:
        verbose_name = _("Webinar Search History")
        verbose_name_plural = _("Webinar Search Histories")
        ordering = ["-updated_at"]

    def __str__(self):
        return self.keyword
