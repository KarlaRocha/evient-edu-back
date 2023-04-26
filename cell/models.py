from django.db import models
from match.models import Match

class Cell(models.Model):
    row = models.SmallIntegerField()
    column = models.SmallIntegerField()
    symbol = models.TextField(blank=True)
    match = models.ForeignKey(Match, on_delete=models.CASCADE)

