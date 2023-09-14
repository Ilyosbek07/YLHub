from django.contrib import admin

from apps.course.models.cource import (Category, Course, CourseCertificate,
                                       CourseReview, UserCourse)
from apps.course.models.lesson import Lesson, LessonContent, LessonView


class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name", "is_optional"]


admin.site.register(Category, CategoryAdmin)


class CourseAdmin(admin.ModelAdmin):
    list_display = ["title", "category", "duration_time", "score"]
    list_filter = ["category"]
    search_fields = ["title"]


admin.site.register(Course, CourseAdmin)


class UserCourseAdmin(admin.ModelAdmin):
    list_display = ["profile", "course", "start_time", "end_time", "is_finish"]
    list_filter = ["is_finish", "course"]
    search_fields = ["profile__user__username", "course__title"]


admin.site.register(UserCourse, UserCourseAdmin)


class CourseCertificateAdmin(admin.ModelAdmin):
    list_display = ["user_course", "certificate"]


admin.site.register(CourseCertificate, CourseCertificateAdmin)


class CourseReviewAdmin(admin.ModelAdmin):
    list_display = ["user_course", "comment", "rating"]
    list_filter = ["rating"]
    search_fields = ["user_course__profile__user__username"]


admin.site.register(CourseReview, CourseReviewAdmin)


class LessonAdmin(admin.ModelAdmin):
    list_display = ["course", "title", "type", "order"]
    list_filter = ["course", "type"]
    search_fields = ["title"]


admin.site.register(Lesson, LessonAdmin)


class LessonContentAdmin(admin.ModelAdmin):
    list_display = ["lesson", "title", "order"]
    list_filter = ["lesson"]
    search_fields = ["title"]


admin.site.register(LessonContent, LessonContentAdmin)


class LessonViewAdmin(admin.ModelAdmin):
    list_display = ["profile", "lesson", "is_finish"]
    list_filter = ["is_finish", "lesson__course"]
    search_fields = ["profile__user__username", "lesson__title"]


admin.site.register(LessonView, LessonViewAdmin)
