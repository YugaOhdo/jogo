from django.contrib import admin
from .model import Player

@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    list_display = 'id', 'username','name', 'cardlist', 'feiticos','par_linha_coluna', 'batalha3lista',
    