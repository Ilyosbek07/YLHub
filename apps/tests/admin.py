from django.contrib import admin
from .models import Test, Question, QuestionContent, Variant, UserTest


class QuestionContentInline(admin.TabularInline):
    model = QuestionContent
    extra = 1  # Number of empty forms to display for QuestionContent when editing Question.


class VariantInline(admin.TabularInline):
    model = Variant
    extra = 1  # Number of empty forms to display for Variant when editing Test.


class QuestionInline(admin.TabularInline):
    model = Question
    extra = 1  # Number of empty forms to display for Question when editing Test.


class TestAdmin(admin.ModelAdmin):
    list_display = ('title', 'course', 'duration_time', 'order', 'is_resubmit')
    inlines = [QuestionInline]


class QuestionAdmin(admin.ModelAdmin):
    list_display = ('test', 'type', 'name', 'order')
    inlines = [VariantInline]


class UserTestAdmin(admin.ModelAdmin):
    list_display = ('user', 'test', 'start_time', 'end_time', 'is_finish')


class VariantAdmin(admin.ModelAdmin):
    list_display = ('name', 'order', 'is_answer')


class QuestionContentAdmin(admin.ModelAdmin):
    list_display = ('id', 'question')


admin.site.register(Test, TestAdmin)
admin.site.register(Variant, VariantAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(UserTest, UserTestAdmin)
admin.site.register(QuestionContent, QuestionContentAdmin)
