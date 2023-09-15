from rest_framework import serializers
from .models import Webinar, WebinarSearchHistory

class WebinarListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Webinar
        fields = ("id", "title", "author", "cover_image", "status")


class WebinarSearchHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = WebinarSearchHistory
        fields = ("id", "keyword")


class WebinarDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Webinar
        fields = (
            "id", 
            "title",
            "author", 
            "cover_image", 
            "status",
            "about",
            "stream_url",
            "webinar_type"
        )
