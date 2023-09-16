from rest_framework import generics

from apps.users.serializers import ProfileSerializer, RegisterUserSerializer
from apps.users.models import Profile, User


class ProfileDetailView(generics.RetrieveAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


class UserCreateAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterUserSerializer
