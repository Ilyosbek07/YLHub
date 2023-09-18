from rest_framework import generics

from apps.course.models import Lesson
from apps.course.serializers.lesson import LessonSerializer, LessonDetailSerializer


class LessonRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonDetailSerializer
