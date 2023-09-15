from rest_framework import generics
from rest_framework.parsers import MultiPartParser

from apps.users.serializers import ProfileSerializer, RegisterUserSerializer, DocumentSerializer, SocialMediaSerializer
from apps.users.models import Profile, User, Document, SocialMedia


class ProfileDetailView(generics.RetrieveAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


class ProfileCreateAPIView(generics.CreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


class UserCreateAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterUserSerializer


class DocumentCreateAPIView(generics.CreateAPIView):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer
    parser_classes = (MultiPartParser,)


class SocialMediaCreateAPIView(generics.CreateAPIView):
    queryset = SocialMedia.objects.all()
    serializer_class = SocialMediaSerializer
