from rest_framework import serializers

from apps.course.models import Category, Course, Lesson, UserCourse
from apps.course.serializers.lesson import LessonSerializer


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ("name",)


#
class CourseSerializer(serializers.ModelSerializer):
    category = CategorySerializer()

    class Meta:
        model = Course
        fields = (
            "id",
            "category",
            "title",
            "desc",
            "duration_day",
            "expired_date",
            "score",
            "main_image",
            'is_optional',
        )


class CourseRetrieveSerializer(serializers.ModelSerializer):
    course_lesson = LessonSerializer(many=True)
    lessons_count = serializers.SerializerMethodField()

    class Meta:
        model = Course
        fields = ("id", "title", "desc", "duration_day", "score", "main_image", "course_lesson", "lessons_count")

    def get_lessons_count(self, obj):
        lessons = Lesson.objects.filter(course=obj.pk)
        return len(lessons)


class UserCourseSerializer(serializers.ModelSerializer):
    course = CourseSerializer()

    class Meta:
        model = UserCourse
        fields = (
            'user',
            'start_time',
            'end_time',
            'is_finish',
            'course',
        )
