from django.urls import path
from .views import MatchList, MatchDetail, MatchCreate

match_urlpatterns = [
    path('matches/', MatchList.as_view(), name='match_list'),
    path('match/', MatchCreate.as_view(), name='create_match'),
    path('matches/<int:pk>/', MatchDetail.as_view(), name='match-detail'),

]
