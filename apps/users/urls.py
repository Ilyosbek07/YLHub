from django.urls import path

from apps.users.views import ProfileDetailView

urlpatterns = [
    path('<int:pk>/detail/', ProfileDetailView.as_view(), name='profile_detail')
]
