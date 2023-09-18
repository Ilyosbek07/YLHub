from rest_framework import generics

from apps.course.models import Lesson
from apps.course.serializers.lesson import LessonDetailSerializer


class LessonRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonDetailSerializer



#So'rash kerak
# class CourseLessonRetrieveAPIView(generics.RetrieveAPIView):
#     queryset = Lesson.objects.all()
#     serializer_class = LessonDetailSerializer
#     lookup_field = 'lesson_id'
#
#     def get_queryset(self):
#         course_id = self.kwargs.get('course_id')
#         return Lesson.objects.filter(course=course_id)

    # path('<int:course_id>/lesson/<int:lesson_id>/detail/', CourseLessonRetrieveAPIView.as_view(), name='course_lesson_detail')
