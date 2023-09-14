from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics

from apps.course.filters import CourseFilter
from apps.course.models import Course
from apps.course.serializers.course import CourseSerializer, CourseRetrieveSerializer


class CourseListAPIView(generics.ListAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = CourseFilter


class CourseRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseRetrieveSerializer
