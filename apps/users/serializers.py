from rest_framework import serializers

from apps.users.models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = (
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
        )
