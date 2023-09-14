from django.urls import path
from .views import (
    MainPageView,
    NewsListView,
    NewsDetailView,
    EventListView,
    EventDetailView,
    PollListView,
    PollDetailView,
    PollChoiceSelectedView
)

urlpatterns = [
    path('main/', MainPageView.as_view(), name='main'),
    path('news/', NewsListView.as_view(), name='news_list'),
    path('news/<int:pk>/', NewsDetailView.as_view(), name='news_detail'),
    path('events/', EventListView.as_view(), name='event_list'),
    path('event/<int:pk>/', EventDetailView.as_view(), name='event_detail'),
    path('polls/', PollListView.as_view(), name='poll_list'),
    path('polls/<int:pk>/', PollDetailView.as_view(), name='poll_detail'),
    path('polls/voted/<int:pk>/', PollChoiceSelectedView.as_view(), name='poll_voted')
]
