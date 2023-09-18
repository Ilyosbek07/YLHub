from django.core.validators import FileExtensionValidator
from django.db import models
from django.utils.translation import gettext as _

from apps.common.models import BaseModel
from apps.users.models import Profile, User


class Category(BaseModel):
    name = models.CharField(max_length=125, verbose_name=_("Name"))

    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")

    def __str__(self):
        return self.name


class Course(BaseModel):
    category = models.ForeignKey(
        Category, related_name="course_category", on_delete=models.CASCADE, verbose_name=_("Category")
    )
    title = models.CharField(max_length=125, verbose_name=_("Title"))
    desc = models.TextField(verbose_name=_("Description"))
    duration_day = models.IntegerField(verbose_name=_("Duration Day"))
    expired_date = models.DateField(verbose_name=_("Expired Date"))
    score = models.IntegerField(verbose_name=_("Score"))
    main_image = models.ImageField(verbose_name=_("Main Image"))
    is_optional = models.BooleanField(default=False, verbose_name=_("Is Optional"))

    class Meta:
        verbose_name = _("Course")
        verbose_name_plural = _("Courses")

    def __str__(self):
        return self.title


class UserCourse(BaseModel):
    user = models.ForeignKey(User, related_name="profile_user_course", verbose_name=_("User"), on_delete=models.CASCADE)
    course = models.ForeignKey(Course, related_name="user_course", verbose_name=_("Course"), on_delete=models.CASCADE)
    start_time = models.DateField(auto_now_add=True)
    end_time = models.DateField(auto_now_add=True)
    is_finish = models.BooleanField(default=False)

    class Meta:
        unique_together = ["user", "course"]
        verbose_name = _("User Course")
        verbose_name_plural = _("User Courses")


class CourseCertificate(BaseModel):
    user_course = models.ForeignKey(
        UserCourse, related_name="user_certificate", verbose_name=_("User Course"), on_delete=models.CASCADE
    )
    certificate = models.FileField(
        upload_to="certificate/",
        validators=[FileExtensionValidator(allowed_extensions=["txt", "csv", "html", "jpg", "jpeg", "png"])],
        verbose_name=_("Certificate"),
    )

    class Meta:
        verbose_name = _("Course Certificate")
        verbose_name_plural = _("Course Certificates")


class CourseReview(BaseModel):
    user_course = models.ForeignKey(
        UserCourse, related_name="review", on_delete=models.CASCADE, verbose_name=_("User Course")
    )
    comment = models.TextField(verbose_name=_("Comment"))
    rating = models.PositiveIntegerField(validators=[], verbose_name=_("Rating"))

    class Meta:
        verbose_name = _("Course Review")
        verbose_name_plural = _("Course Reviews")
