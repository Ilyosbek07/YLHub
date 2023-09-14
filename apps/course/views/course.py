from rest_framework import generics

from apps.course.models import Course
from apps.course.serializers.course import CourseSerializer, CourseRetrieveSerializer


class CourseListAPIView(generics.ListAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class CourseRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseRetrieveSerializer
