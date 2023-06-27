from django.urls import path
from .views import MatchList, MatchDetail, MatchCreate, PlayerMove, PlayerWinner

match_urlpatterns = [
    path('matches/', MatchList.as_view(), name='match_list'),
    path('match/', MatchCreate.as_view(), name='create_match'),
    path('match/winner/<int:pk>/', PlayerWinner.as_view(), name='match_winner'),
    path('match/player-move/<int:pk>/', PlayerMove.as_view(), name='player_move'),
    path('matches/<int:pk>/', MatchDetail.as_view(), name='match_detail'),
]
