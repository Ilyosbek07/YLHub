from rest_framework import serializers

from apps.course.models import Course, Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('name', 'is_optional')


class CourseSerializer(serializers.ModelSerializer):
    category = CategorySerializer()

    class Meta:
        model = Course
        fields = (
            'category',
            'title',
            'desc',
            'duration_time',
            'score',
            'main_image'
        )


class CourseRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = (
            'category',
            'title',
            'desc',
            'duration_time',
            'score',
            'main_image'
        )
