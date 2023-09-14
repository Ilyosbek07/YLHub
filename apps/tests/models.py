from django.core.validators import FileExtensionValidator
from django.db import models
from django.utils.translation import gettext as _

from apps.common.models import BaseModel
from apps.course.models import Course
from apps.users.models import User


class Test(BaseModel):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name=_("Course"),
                               related_name='course_test')
    title = models.CharField(max_length=125, verbose_name=_("title"))
    duration_time = models.IntegerField(_("Duration Time"))
    order = models.IntegerField(verbose_name=_("Order"))
    is_resubmit = models.BooleanField(default=False, verbose_name=_('Is Resubmit'))

    class Meta:
        verbose_name = _("Test")
        verbose_name_plural = _("Tests")

    def __str__(self):
        return self.title


class Question(BaseModel):
    class Type(models.TextChoices):
        choice_order = 'order', _("Choice Order")
        MULTI_SELECT = 'multi', _("Multi Select")
        SINGLE_SELECT = 'single', _("Single Select")

    test = models.ForeignKey(Test, on_delete=models.CASCADE, verbose_name=_("Test"), related_name='test_question')
    type = models.CharField(max_length=125, choices=Type.choices, verbose_name=_('Type'))
    name = models.TextField(verbose_name=_("Text"))
    order = models.IntegerField(verbose_name=_("Order"))

    class Meta:
        verbose_name = _("Question")
        verbose_name_plural = _("Questions")

    def __str__(self):
        return f"Question for {self.test} - Order: {self.order}"


class QuestionContent(BaseModel):
    question = models.ForeignKey(
        Question,
        related_name='question_content',
        on_delete=models.CASCADE,
        verbose_name=_('Question')
    )
    file = models.FileField(
        upload_to='test_question/',
        validators=[FileExtensionValidator(
            allowed_extensions=['jpg', 'jpeg', 'png', 'gif', 'mp3', 'wav', 'ogg', 'mp4', 'avi', 'mov'])],
        verbose_name=_('File')
    )

    class Meta:
        verbose_name = _("Question Content")
        verbose_name_plural = _("Questions Contents")


class Variant(BaseModel):
    question = models.ForeignKey(
        Question,
        on_delete=models.CASCADE,
        verbose_name=_("Question"),
        related_name='question_variant'
    )
    name = models.TextField(verbose_name=_("name"))
    order = models.IntegerField(verbose_name=_("Order"))
    is_answer = models.BooleanField(default=False, verbose_name=_("Is Answer"))

    class Meta:
        verbose_name = _("Variant")
        verbose_name_plural = _("Variants")

    def __str__(self):
        return f"Question Variant {self.name}"


class UserTest(BaseModel):
    user = models.ForeignKey(
        User,
        related_name='user_test',
        on_delete=models.CASCADE,
        verbose_name=_("User")
    )
    test = models.ForeignKey(
        Test,
        related_name='test',
        on_delete=models.CASCADE
    )
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    is_finish = models.BooleanField(default=False, verbose_name=_('Is Finish'))

    def __str__(self):
        return f"{self.user.username}-{self.test.title}"

    class Meta:
        verbose_name = _("User Test")
        verbose_name_plural = _("User Tests")


class UserAnswer(BaseModel):
    user = models.ForeignKey(
        User,
        related_name='user_answer',
        on_delete=models.CASCADE,
        verbose_name=_("User")
    )
    question = models.ForeignKey(
        Question,
        on_delete=models.CASCADE,
        verbose_name=_("Question"),
        related_name='user_question_answer'
    )
    selected_variant = models.ManyToManyField(
        Variant,
        related_name='user_variant'
    )
    is_true = models.BooleanField(default=False, verbose_name=_('Is True'))

    def __str__(self):
        return f"{self.user.username}-answers"

    class Meta:
        verbose_name = _("User Answer")
        verbose_name_plural = _("User Answers")
