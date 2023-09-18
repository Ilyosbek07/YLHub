from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, status
from rest_framework.response import Response

from apps.course.filters import CourseFilter
from apps.course.models import Course, UserCourse, Category
from apps.course.serializers.course import CourseRetrieveSerializer, CourseSerializer, UserCourseSerializer, \
    CategorySerializer
from apps.users.models import User


class CategoryListAPIView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


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


class UserCourseCreateAPIView(generics.CreateAPIView):
    queryset = UserCourse.objects.all()

    def create(self, serializer, *args, **kwargs):
        pk = self.kwargs.get('pk')
        course = Course.objects.get(id=pk)
        UserCourse.objects.create(
            user=self.request.user,
            course=course
        )
        return Response(status=status.HTTP_201_CREATED)
