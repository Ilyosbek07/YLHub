from django.urls import path
from .views import (
    SeminarListView, LectureListView,
    WebinarDetailView, WebinarSearchHistoryView,
    SearchHistoryDeleteView, SearchKeywordAddView
)

urlpatterns = [
    path("seminars/", SeminarListView.as_view(), name="seminar_list"),
    path("lectures/", LectureListView.as_view(), name="lecture_list"),
    path("<int:pk>/", WebinarDetailView.as_view(), name="webinar_detail"),
    path("search-history/", WebinarSearchHistoryView.as_view(), name="search_history"),
    path(
        "search-history/delete/", SearchHistoryDeleteView.as_view(),
        name="search_history_delete"
    ),
    path(
        "search-keyword/add/", SearchKeywordAddView.as_view(),
        name="search_keyword_add"
    )
]
