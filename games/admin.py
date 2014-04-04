from django.contrib import admin
from games.models import Game

class GameAdmin(admin.ModelAdmin):
        list_display = ['game_title', 'onsale', 'rrp', 'drp']
        list_filter = ['rrp', 'drp', 'onsale']
        search_fields = ['game_title']
        
admin.site.register(Game,GameAdmin)
