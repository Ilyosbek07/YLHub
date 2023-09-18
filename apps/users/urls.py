from django.urls import path

from apps.users.views import (
    ProfileDetailView,
    UserCreateAPIView,
    ProfileCreateAPIView,
    DocumentCreateAPIView,
    SocialMediaCreateAPIView, ProfileUpdateAPIView,
)
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path("document/create/", DocumentCreateAPIView.as_view(), name="document_create"),
    path("socialmedia/create/", SocialMediaCreateAPIView.as_view(), name="social_media_create"),

    path("profile/create/", ProfileCreateAPIView.as_view(), name="profile_create"),
    path("profile/<int:pk>/update/", ProfileUpdateAPIView.as_view(), name="profile_update"),
    path("<int:pk>/detail/", ProfileDetailView.as_view(), name="profile_detail"),

    path("register/", UserCreateAPIView.as_view(), name="register"),
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]
