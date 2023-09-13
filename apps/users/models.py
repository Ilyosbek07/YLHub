from django.contrib.auth.hashers import make_password
from django.core.exceptions import ValidationError
from django.db import models
from django.utils.translation import gettext as _
from django.contrib.auth.models import UserManager as AbstractUserManager, AbstractUser, Permission, Group
from apps.common.models import BaseModel


class UserManager(AbstractUserManager):
    def _create_user(self, phone_number, password, **extra_fields):
        """
        Create and save a user with the given phone_number and password.
        """
        if not phone_number:
            raise ValueError("The given phone number must be set")

        user = self.model(phone_number=phone_number, **extra_fields)
        user.password = make_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, phone_number, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")
        return self._create_user(phone_number, password, **extra_fields)

    def create_user(self, phone_number, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(phone_number, password, **extra_fields)


class User(AbstractUser, BaseModel):
    phone_number = models.CharField(
        verbose_name=_("Phone number"),
        max_length=16,
        unique=True,
    )
    email = models.EmailField(verbose_name=_("Email"), null=True, blank=True)

    """
    password_set:
        We set this to False when user is registered with social auth.  Because we don't get password in social auth.
        we send this in user details to frontend. So that frontend shows "set password" button instead of "change
        password" set to True when user sets password
    """
    password_set = models.BooleanField(default=True, editable=False)

    password_changed_at = models.DateTimeField(null=True, blank=True)

    objects = UserManager()

    USERNAME_FIELD = "username"
    groups = models.ManyToManyField(
        Group,
        verbose_name=_('groups'), blank=True,
        help_text=_('The groups this user belongs to.'), related_name='custom_user_set'
        # Change this to a unique name
    )
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name=_('user permissions'), blank=True,
        help_text=_('Specific permissions for this user.'),
        related_name='custom_user_set'  # Change this to a unique name
    )

    class Meta:
        db_table = "user"
        verbose_name = _("User")
        verbose_name_plural = _("Users")

    def __str__(self):
        return self.phone_number

    def save(self, *args, **kwargs):
        if self.phone_number:
            user = User.objects.filter(phone_number=self.phone_number).first()
            if user and user.id != self.id:
                raise ValidationError(_("User with this phone number already exists."))
        super().save(*args, **kwargs)


class Profile(BaseModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    full_name = models.CharField(max_length=255, verbose_name=_('Full Name'))
    position = models.CharField(max_length=255, verbose_name=_('Position'))
    JShShIR = models.CharField(max_length=255, verbose_name=_('JShShIR'))
    study_center = models.CharField(max_length=255, verbose_name=_('Study Center'))
    passport_series = models.CharField(max_length=255, verbose_name=_('Passport Series'))
    NATIONALITY_CHOICES = (
        ('us', _('United States')),
        ('uz', _('Uzbek')),
        ('ru', _('Russian')),
    )
    nationality = models.CharField(max_length=255, choices=NATIONALITY_CHOICES, verbose_name=_('Nationality'))

    DEGREE_CHOICES = (
        ('bsc', _('Bachelor')),
        ('msc', _('Master')),
        ('stu', _('Student')),
    )
    degree = models.CharField(max_length=55, choices=DEGREE_CHOICES, verbose_name=_('Degree'))
    birth_date = models.DateField(verbose_name=_("Birth date"), null=True, blank=True)
    score = models.IntegerField(verbose_name=_("Score"))

    class Meta:
        verbose_name = _('Profile')
        verbose_name_plural = _('Profiles')

    def __str__(self):
        return self.full_name


class Document(BaseModel):
    profile = models.ForeignKey(Profile, related_name='profile_documents', verbose_name=_('Profile'),
                                on_delete=models.CASCADE)
    type = models.CharField(max_length=125, verbose_name=_('Type'))
    name = models.CharField(max_length=125, verbose_name=_('Name'))
    file = models.FileField(upload_to='media/documents', verbose_name=_('Document'))

    class Meta:
        verbose_name = _('Document')
        verbose_name_plural = _('Documents')

    def __str__(self):
        return self.name


class SocialMedia(BaseModel):
    profile = models.ForeignKey(Profile, related_name='profile_social_media', verbose_name=_('Profile'),
                                on_delete=models.CASCADE)
    link = models.URLField(verbose_name=_('Link'))

    class Meta:
        verbose_name = _('Social Media')
        verbose_name_plural = _('Social Media')

    def __str__(self):
        return self.link
