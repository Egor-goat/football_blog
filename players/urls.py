from django.urls import path
from . import views


urlpatterns = [
    path('', views.show_players, name="player_list"),
    path("add/",views.add_player, name="add_player"),
    path("edit/<int:pk>/", views.edit_player, name='edit_player'),
    path("delete/<int:pk>/", views.delete_player, name='delete_player'),
    path("teams/", views.team_list, name='team_list'),
    path("teams/<int:pk>/", views.team_detail, name='team_detail'),
    path("season/", views.season_view, name='season'),
    path("league/", views.league_table_view, name="league_table"),
]