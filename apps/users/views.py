from rest_framework import generics

from apps.users.serializers import ProfileSerializer
from apps.users.models import Profile


class ProfileDetailView(generics.RetrieveAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
