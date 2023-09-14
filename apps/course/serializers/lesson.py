from rest_framework import serializers

from apps.course.models import Lesson


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = (
           'title',
           'description',
           'type',
           'order',
        )
