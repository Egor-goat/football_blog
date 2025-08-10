from django.contrib import admin
from .models import Player, Team, LeagueTable

@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    list_display = ("name", "age", "position")

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ("name", "country", "founded")

@admin.register(LeagueTable)
class LeagueTableAdmin(admin.ModelAdmin):
    list_display = ('team', 'played', 'wins', 'draws', 'losses', 'goals_for', 'goals_against', 'points')