from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics

from apps.course.filters import CourseFilter
from apps.course.models import Course, UserCourse
from apps.course.serializers.course import CourseRetrieveSerializer, CourseSerializer, UserCourseSerializer
from apps.users.models import User


class CourseListAPIView(generics.ListAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = CourseFilter


class CourseRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseRetrieveSerializer


class UserCourseListAPIView(generics.ListAPIView):
    serializer_class = UserCourseSerializer

    def get_queryset(self):
        pk = self.kwargs.get("pk")
        return UserCourse.objects.filter(user=pk)


class UserCourseRetrieveAPIView(generics.RetrieveAPIView):
    queryset = UserCourse.objects.all()
    serializer_class = UserCourseSerializer
