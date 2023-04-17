from django.urls import path
from .views import MatchList, MatchDetail

match_urlpatterns = [
    path('matches/', MatchList.as_view(), name='match_list'),
    path('matches/<int:pk>/', MatchDetail.as_view(), name='match-detail')
]
