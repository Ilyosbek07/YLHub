from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken

from apps.users.models import Profile, User, Document, SocialMedia


class RegisterUserSerializer(serializers.ModelSerializer):
    token = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = [
            "username",
            "password",
            "token",
        ]
        extra_kwargs = {
            "password": {"write_only": True},
            "token": {"read_only": True},
        }

    def get_token(self, user):
        tokens = RefreshToken.for_user(user)
        data = {"refresh": str(tokens), "access": str(tokens.access_token)}
        return data


class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = (
            "profile",
            "type",
            "name",
            "certificate",
        )


class SocialMediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialMedia
        fields = (
            "profile",
            "link",
        )


class ProfileSerializer(serializers.ModelSerializer):
    profile_documents = DocumentSerializer(many=True)

    class Meta:
        model = Profile
        fields = (
            "id",
            "user",
            "full_name",
            "position",
            "JShShIR",
            "study_center",
            "passport_series",
            "nationality",
            "degree",
            "birth_date",
            "score",
            "profile_documents",
        )


class ProfileCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = (
            "full_name",
            "position",
            "JShShIR",
            "study_center",
            "passport_series",
            "nationality",
            "degree",
            "birth_date",
        )
