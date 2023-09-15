from django.db import models
from django.db.models import F, Case, When, ExpressionWrapper
from rest_framework import serializers

from .models import News, Poll, Event, PollChoice

class MainPageSerializer(serializers.ModelSerializer):
    time = serializers.DateTimeField()
    tags = serializers.StringRelatedField(many=True)
    type = serializers.CharField()

    class Meta:
        model = News
        fields = (
            'id',
            'updated_at',
            'title',
            'slug',
            'cover_image',
            'time',
            'tags',
            'type'
        )


class NewsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = (
            'id',
            'updated_at',
            'title',
            'slug',
            'cover_image',
            'tags',
        )


class NewsDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = (
            'id',
            'updated_at',
            'title',
            'slug',
            'cover_image',
            'tags',
            'body',
        )


class EventListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = (
            'id',
            'updated_at',
            'title',
            'slug',
            'cover_image',
            'time',
        )


class EventDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = (
            'id',
            'updated_at',
            'title',
            'slug',
            'cover_image',
            'time',
            'location',
            'about'
        )


class PollListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Poll
        fields = (
            'id',
            'updated_at',
            'title',
            'slug',
            'cover_image'
        )


class PollUncompletedChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = PollChoice
        fields = ("id", "order", "text")


class PollCompletedChoiceSerializer(serializers.ModelSerializer):
    is_selected = serializers.BooleanField()
    percentage = serializers.FloatField()
    class Meta:
        model = PollChoice
        fields = ("id", "order", "text", "is_selected", "percentage")


class PollUncompletedDetailSerializer(serializers.ModelSerializer):
    choices = PollUncompletedChoiceSerializer(many=True)
    total_votes = serializers.SerializerMethodField()
    class Meta:
        model = Poll
        fields = (
            'id',
            'updated_at',
            'title',
            'slug',
            'cover_image',
            'total_votes',
            'choices'
        )

    def get_total_votes(self, obj):
        return obj.get_total_votes()


class PollCompletedDetailSerializer(serializers.ModelSerializer):
    total_votes = serializers.SerializerMethodField()
    choices = serializers.SerializerMethodField()
    class Meta:
        model = Poll
        fields = (
            'id',
            'updated_at',
            'title',
            'slug',
            'cover_image',
            'total_votes',
            'choices'
        )

    def get_total_votes(self, obj):
        return obj.get_total_votes()

    def get_choices(self, obj):
        selected = self.context.get('selected')
        choices = obj.choices
        total_votes = obj.get_total_votes()
        choices = choices.annotate(
            is_selected=Case(
                When(id=selected, then=True),
                default=False,
                output_field=models.BooleanField()
            ),
            percentage=ExpressionWrapper(F('votes') * 100.0 / total_votes, output_field=models.FloatField())
        )
        return PollCompletedChoiceSerializer(choices, many=True).data
