from django.db import models

class Player(models.Model):
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    score = models.IntegerField(null=True, blank=True, default=0)
    wins = models.IntegerField(null=True, blank=True, default=0)
    loses = models.IntegerField(null=True, blank=True, default=0)
    draws = models.IntegerField(null=True, blank=True, default=0) 

