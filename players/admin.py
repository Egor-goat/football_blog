from django.contrib import admin
from .models import Player, Team

@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    list_display = ("name", "age", "position")

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ("name", "country", "founded")
    