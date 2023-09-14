from django.db.models import TextChoices
from django.utils.translation import gettext_lazy as _

class WebinarStatusChoices(TextChoices):
    LIVE = "l", _("Live")
    COMPLETED = "c", _("Completed")
    PLANNED = "p", _("Planned")


class WebinarTypeChoices(TextChoices):
    LECTURE = "l", _("Lecture")
    SEMINAR = "s", _("Seminar")


class ComplaintTypeChoices(TextChoices):
    ILLEGAL = "i", _("Illegal")
    PERSONAL = "p", _("Personal")
    AD = "a", _("Ad")
    FAKE = "f", _("Fake")
    OTHER = "o", _("Other")
    