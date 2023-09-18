from django.urls import path

from apps.course.views.course import CourseListAPIView, CourseRetrieveAPIView, UserCourseListAPIView, \
    UserCourseRetrieveAPIView, UserCourseCreateAPIView, CategoryListAPIView
from apps.course.views.lesson import LessonRetrieveAPIView

urlpatterns = [
    path('category/list/', CategoryListAPIView.as_view(), name='category_list'),

    # Course Urls
    path('list/', CourseListAPIView.as_view(), name='course_list'),
    path('<int:pk>/detail/', CourseRetrieveAPIView.as_view(), name='course_detail'),

    # User Course Urls
    path('<int:pk>/submit/', UserCourseCreateAPIView.as_view(), name='user_course_create_list'),
    path('list/user/<int:pk>/', UserCourseListAPIView.as_view(), name='user_course_list'),
    path('user/<int:pk>/detail/', UserCourseRetrieveAPIView.as_view(), name='user_course_detail'),

    # Lesson urls
    path('<int:pk>/lesson/', LessonRetrieveAPIView.as_view(), name='lesson_detail'),

]
