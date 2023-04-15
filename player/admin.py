from django.contrib import admin
from .models import Player

class PlayerAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'score', 'wins', 'loses', 'draws')

admin.site.register(Player, PlayerAdmin)
