from itertools import chain
from datetime import datetime
from django.db import models
from django.db.models import Value
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import ListAPIView, RetrieveAPIView

from .models import News, Event, Poll, UserPoll, Tag, PollChoice
from .serializers import (
    MainPageSerializer,
    NewsListSerializer,
    NewsDetailSerializer,
    EventListSerializer,
    EventDetailSerializer,
    PollListSerializer,
    PollUncompletedDetailSerializer,
    PollCompletedDetailSerializer
)

class MainPageView(ListAPIView):
    queryset = News.objects.all()
    serializer_class = MainPageSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        news = News.objects.filter(is_active=True).annotate(
            type=Value("news", output_field=models.CharField(max_length=255)),
            time=Value(None, output_field=models.DateTimeField())
        ).only(
            'id', 'updated_at', 'title',
            'slug', 'cover_image', 'tags'
        )
        current_time = datetime.now()
        events = Event.objects.filter(time__gte=current_time).annotate(
            type=Value("event", output_field=models.CharField(max_length=255)),
            tags=Value(None, output_field=models.ManyToManyField(to=Tag))
        ).only(
            'id', 'updated_at', 'title',
            'slug', 'cover_image', 'time'
        )
        polls = Poll.objects.filter(is_active=True).annotate(
            type=Value("poll", output_field=models.CharField(max_length=255)),
            time=Value(None, output_field=models.DateTimeField()),
            tags=Value(None, output_field=models.ManyToManyField(to=Tag))
        ).only(
            'id', 'updated_at', 'title',
            'slug', 'cover_image'
        )
        combined = chain(news, events, polls)
        return sorted(combined, key=lambda h: h.updated_at, reverse=True)


class NewsListView(ListAPIView):
    model_class = News
    queryset = News.objects.all()
    serializer_class = NewsListSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(is_active=True)


class NewsDetailView(RetrieveAPIView):
    model_class = News
    queryset = News.objects.all()
    serializer_class = NewsDetailSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(is_active=True)


class EventListView(ListAPIView):
    model_class = Event
    queryset = Event.objects.all()
    serializer_class = EventListSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        current_time = datetime.now()
        return self.queryset.filter(time__gte=current_time)


class EventDetailView(RetrieveAPIView):
    model_class = Event
    queryset = Event.objects.all()
    serializer_class = EventDetailSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        current_time = datetime.now()
        return self.queryset.filter(time__gte=current_time)


class PollListView(ListAPIView):
    model_class = Poll
    queryset = Poll.objects.all()
    serializer_class = PollListSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(is_active=True)


class PollDetailView(RetrieveAPIView):
    model_class = Poll
    queryset = Poll.objects.all()
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(is_active=True)

    def get_serializer_class(self):
        id = self.kwargs.get('pk')
        choice = UserPoll.objects.filter(choice__poll=id, profile__user=self.request.user)
        if choice.exists():
            self.selected_id = choice.first()
            return PollCompletedDetailSerializer
        else:
            return PollUncompletedDetailSerializer

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['selected'] = self.selected_id
        return context


class PollChoiceSelectedView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        poll_choice = get_object_or_404(PollChoice, pk=pk)
        UserPoll.objects.create(profile=self.request.user.profile, poll=poll_choice)
        poll_choice.votes += 1
        poll_choice.save()
        return Response({'poll': poll_choice.poll.id})
