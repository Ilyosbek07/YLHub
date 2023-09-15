from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import filters
from rest_framework import status
from .models import Webinar, WebinarSearchHistory
from .choices import WebinarTypeChoices
from .serializers import (
    WebinarListSerializer,
    WebinarDetailSerializer,
    WebinarSearchHistorySerializer
)

class SeminarListView(ListAPIView):
    queryset = Webinar.objects.all()
    serializer_class = WebinarListSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [filters.SearchFilter]
    search_fields = ['title']

    def get_queryset(self):
        seminars = self.queryset.filter(webinar_type=WebinarTypeChoices.SEMINAR).order_by("-updated_at")
        return seminars
    

class LectureListView(ListAPIView):
    queryset = Webinar.objects.all()
    serializer_class = WebinarListSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [filters.SearchFilter]
    search_fields = ['title']

    def get_queryset(self):
        lectures = self.queryset.filter(webinar_type=WebinarTypeChoices.LECTURE).order_by("-updated_at")
        return lectures
    

class WebinarDetailView(RetrieveAPIView):
    queryset = Webinar.objects.all()
    serializer_class = WebinarDetailSerializer
    permission_classes = [IsAuthenticated]


class WebinarSearchHistoryView(ListAPIView):
    queryset = WebinarSearchHistory.objects.all()
    serializer_class = WebinarSearchHistorySerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        keywords = self.queryset.filter(profile=self.request.user.profile).order_by("-updated_at")
        return keywords
    

class SearchHistoryDeleteView(RetrieveAPIView):
    queryset = WebinarSearchHistory.objects.all()
    serializer_class = WebinarSearchHistorySerializer
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        keywords = self.queryset.filter(profile=self.request.user.profile).order_by("-updated_at")
        keywords.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

class SearchKeywordAddView(CreateAPIView):
    queryset = WebinarSearchHistory.objects.all()
    serializer_class = WebinarSearchHistorySerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        data = request.data
        WebinarSearchHistory.objects.get_or_create(
            keyword=data['keyword'],
            profile=self.request.user.profile
        )
        return Response(status=status.HTTP_201_CREATED)
