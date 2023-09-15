from django.urls import path

from apps.course.views.course import CourseListAPIView, CourseRetrieveAPIView, UserCourseListAPIView, \
    UserCourseRetrieveAPIView

urlpatterns = [
    # Course Urls
    path('list/', CourseListAPIView.as_view(), name='course_list'),
    path('<int:pk>/detail/', CourseRetrieveAPIView.as_view(), name='course_detail'),

    # User Course Urls
    path('list/user/<int:pk>/', UserCourseListAPIView.as_view(), name='user_course_list'),
    path('detail/user/<int:pk>/', UserCourseRetrieveAPIView.as_view(), name='user_course_detail')
]
