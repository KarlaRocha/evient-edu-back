from django.db import models
from player.models import Player

class Match(models.Model):
    created_date = models.DateField()
    updated_date = models.DateField()
    player_1 = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='player1_matches')
    player_2 = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='player2_matches')
    turn = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='current_turn')
    winner = models.ForeignKey(Player, on_delete=models.CASCADE, blank=True, null=True, default=None, related_name="winner")
    symbol = models.TextField()
    active = models.BooleanField(default=True)
    is_draw = models.BooleanField(default=False)

