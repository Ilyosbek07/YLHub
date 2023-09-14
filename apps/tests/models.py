from django.db import models
from django.utils.translation import gettext as _


class Subject(models.Model):
    name = models.CharField(max_length=125, verbose_name=_("Name"))

    class Meta:
        verbose_name = _("Subject")
        verbose_name_plural = _("Subjects")

    def __str__(self):
        return self.name


class Test(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, verbose_name=_("Subject"),
                                related_name='subject_test')
    duration_time = models.IntegerField(_("Duration Time"), null=True, blank=True)
    order = models.IntegerField(_("Order"))

    class Meta:
        verbose_name = _("Test")
        verbose_name_plural = _("Tests")

    def __str__(self):
        return f"Test for {self.subject} - Order: {self.order}"


class Question(models.Model):
    test = models.ForeignKey(Test, on_delete=models.CASCADE, verbose_name=_("Test"), related_name='question_test')
    text = models.TextField(verbose_name=_("Text"))
    order = models.IntegerField(_("Order"))

    class Meta:
        verbose_name = _("Question")
        verbose_name_plural = _("Questions")

    def __str__(self):
        return f"Question for {self.test} - Order: {self.order}"


class QuestionAnswer(models.Model):
    test = models.ForeignKey(Test, on_delete=models.CASCADE, verbose_name=_("Test"), related_name='question_answer')
    answer = models.TextField(verbose_name=_("Text"))
    order = models.IntegerField(_("Order"))

    class Meta:
        verbose_name = _("Question")
        verbose_name_plural = _("Questions")

    def __str__(self):
        return f"Question Answer for {self.test} - Order: {self.order}"
