from django.urls import path
from .views import (
    BookListView,
    BookDetailView,
    BookFileView,
    BookReadProgressUpdateView,
    AudiobookListView,
    AudiobookDetailView,
    AudiobookFileView,
    AudiobookListenProgressUpdateView,
    PopularCategoriesView,
    CategoryDetailView
)

urlpatterns = [
    path("ebooks/", BookListView.as_view(), name="ebook_list"),
    path("ebooks/<int:pk>", BookDetailView.as_view(), name="ebook_detail"),
    path("ebooks/file/<int:pk>/", BookFileView.as_view(), name="ebook_file"),
    path(
        "ebook_progresses/update/<int:pk>/", BookReadProgressUpdateView.as_view(),
        name="ebook_progress_update" 
    ),
    path("audiobooks/", AudiobookListView.as_view(), name="audiobook_list"),
    path("audiobooks/<int:pk>", AudiobookDetailView.as_view(), name="audiobook_detail"),
    path("audiobooks/file/<int:pk>/", AudiobookFileView.as_view(), name="audiobook_file"),
    path(
        "audiobook_progresses/update/<int:pk>/", AudiobookListenProgressUpdateView.as_view(),
        name="audiobook_progress_update" 
    ),
    path("categories/popular/", PopularCategoriesView.as_view(), name="popular_categories"),
    path("categories/<int:pk>/", CategoryDetailView.as_view(), name="category_detail")
]