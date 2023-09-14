from django.urls import path

from apps.course.views.course import CourseListAPIView, CourseRetrieveAPIView

urlpatterns = [
    path('list/', CourseListAPIView.as_view(), name='course_list'),
    path('<int:pk>/detail/', CourseRetrieveAPIView.as_view(), name='course_detail')
]
