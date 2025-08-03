from django.shortcuts import render
from .models import Player, Team

from .forms import PlayerForm
from django.shortcuts import render, redirect

from django.shortcuts import get_object_or_404

def show_players(request):
    players = Player.objects.all()
    return render(request,"players/players.html",{"players":players})

def season_view(request):
    players = Player.objects.select_related('team').all().order_by('-goals', '-assists')
    return render(request, 'players/season.html', {'players': players})

def add_player(request):
    if request.method == 'POST':
        form = PlayerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("player_list")
    else:
        form = PlayerForm()

    return render(request, 'players/add_player.html', {'form': form})

def edit_player(request, pk):
    player = get_object_or_404(Player, pk=pk)
    if request.method == 'POST':
        form = PlayerForm(request.POST, instance=player)
        if form.is_valid():
            form.save()
            return redirect('player_list')
    else:
        form = PlayerForm(instance=player)

    return render(request, 'players/edit_player.html', {'form': form, 'player': player})

def delete_player(request, pk):
    player = get_object_or_404(Player, pk=pk)
    if request.method == 'POST':
        player.delete()
        return redirect('player_list')
    return render(request, 'players/delete_player.html', {'player': player})

def team_list(request):
    teams = Team.objects.all()

    return render(request, 'players/team_list.html', {'teams': teams})


def team_detail(request, pk):
    team = get_object_or_404(Team, pk=pk)
    players = team.players.all()

    return render(request, 'players/team_detail.html', {'team': team, 'players': players})

