from django.urls import path
from .views import PlayerList, PlayerDetail

player_urlpatterns = [
    path('players/', PlayerList.as_view(), name='player-list'),
    path('players/<int:pk>/', PlayerDetail.as_view(), name='player-detail'),
]
