from django.contrib import admin
from .models import Match

class MatchAdmin(admin.ModelAdmin):
    list_display = ('updated_date', 'player_1', 'player_2', 'winner', 'is_draw', 'active')
    
admin.site.register(Match, MatchAdmin)
