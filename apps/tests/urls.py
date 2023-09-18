from django.urls import path

from apps.tests.views import TestListAPIView

urlpatterns = [
    path('course/<int:pk>/', TestListAPIView.as_view(), name='course_tests')
]
