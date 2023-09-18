from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError
from django.shortcuts import get_object_or_404
from rest_framework.generics import ListAPIView, RetrieveAPIView, UpdateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import (
    Book,
    UserBookProgress,
    AudioBook,
    UserAudiobookProgress,
    BookCategory
)
from .serializers import (
    BookListSerializer,
    BookReadInDetailSerializer,
    BookUnreadDetailSerializer,
    BookFileSerializer,
    BookReadProgressSerializer,
    AudiobookListSerializer,
    AudiobookListenedDetailSerializer,
    AudiobookUnlistenedDetailSerializer,
    AudiobookFileSerializer,
    AudiobookListenProgressSerializer,
    PopularCategoriesSerializer,
    CategoryDetailSerializer
)

class BookListView(ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookListSerializer
    permission_classes = [IsAuthenticated]


class BookDetailView(RetrieveAPIView):
    queryset = Book.objects.all()
    permission_classes = [IsAuthenticated]

    def retrieve(self, request, *args, **kwargs):
        profile = self.request.user.profile
        book_progress = profile.book_progresses.filter(
            book__id=self.kwargs["pk"]
        )
        if book_progress.exists():
            serializer = BookReadInDetailSerializer(book_progress.first())
        else:
            book = get_object_or_404(Book, pk=self.kwargs["pk"])
            serializer = BookUnreadDetailSerializer(book)
        return Response(serializer.data)


class BookFileView(RetrieveAPIView):
    queryset = UserBookProgress.objects.all()
    serializer_class = BookFileSerializer
    permission_classes = [IsAuthenticated]

    def retrieve(self, request, *args, **kwargs):
        profile = self.request.user.profile
        book = get_object_or_404(Book, pk=self.kwargs["pk"])
        book_progress = profile.book_progresses.filter(
            book=book
        )
        if book_progress.exists():
            progress =  book_progress.first()
        else:
            progress = UserBookProgress.objects.create(
                profile=profile, book=book, last_page=0    
            )
        serializer = self.get_serializer(progress)
        return Response(serializer.data)


class BookReadProgressUpdateView(UpdateAPIView):
    queryset = UserBookProgress.objects.all()
    serializer_class = BookReadProgressSerializer
    permission_classes = [IsAuthenticated]


class AudiobookListView(ListAPIView):
    queryset = AudioBook.objects.all()
    serializer_class = AudiobookListSerializer
    permission_classes = [IsAuthenticated]


class AudiobookDetailView(RetrieveAPIView):
    queryset = AudioBook.objects.all()
    permission_classes = [IsAuthenticated]

    def retrieve(self, request, *args, **kwargs):
        profile = self.request.user.profile
        audiobook_progress = profile.audiobook_progresses.filter(
            audiobook__id=self.kwargs["pk"]
        )
        if audiobook_progress.exists():
            serializer =  AudiobookListenedDetailSerializer(
                audiobook_progress.first()
            )
        else:
            audiobook = get_object_or_404(AudioBook, pk=self.kwargs["pk"])
            serializer = AudiobookUnlistenedDetailSerializer(
                audiobook
            )
        return Response(serializer.data)


class AudiobookFileView(RetrieveAPIView):
    queryset = UserAudiobookProgress
    serializer_class = AudiobookFileSerializer
    permission_classes = [IsAuthenticated]

    def retrieve(self, request, *args, **kwargs):
        profile = self.request.user.profile
        audiobook = get_object_or_404(AudioBook, pk=self.kwargs["pk"])
        audiobook_progress = profile.audiobook_progresses.filter(
            audiobook=audiobook
        )
        if audiobook_progress.exists():
            progress = audiobook_progress.first()
        else:
            try:
                unit = audiobook.sections.first().units.first()
                progress =  UserAudiobookProgress.objects.create(
                    profile=profile, audio_unit=unit 
                )
            except:
                raise ValidationError(_("Invalid file"))
        serializer = self.get_serializer(progress)
        return Response(serializer.data)


class AudiobookListenProgressUpdateView(UpdateAPIView):
    queryset = UserAudiobookProgress.objects.all()
    serializer_class = AudiobookListenProgressSerializer
    permission_classes = [IsAuthenticated]


class PopularCategoriesView(ListAPIView):
    queryset = BookCategory.objects.all()
    serializer_class = PopularCategoriesSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(is_popular=True)


class CategoryDetailView(RetrieveAPIView):
    queryset = BookCategory.objects.all()
    serializer_class = CategoryDetailSerializer
    permission_classes = [IsAuthenticated]
