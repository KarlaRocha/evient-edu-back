from django.contrib import admin
from .models import Cell

class CellAdmin(admin.ModelAdmin):
    list_display = ('match', 'row', 'column')

admin.site.register(Cell, CellAdmin)
