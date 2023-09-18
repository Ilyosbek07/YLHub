from django.db.models import TextChoices
from django.utils.translation import gettext_lazy as _

class LanguageChoices(TextChoices):
    UZBEK = "uz", _("Uzbek")
    RUSSIAN = "ru", _("Russian")
    ENGLISH = "en", _("English")
    