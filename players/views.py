from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import VolleyballPlayer
from .forms import VolleyballPlayerForm

def player_list(request):
    """Read - Display all players"""
    players = VolleyballPlayer.objects.all()
    return render(request, 'players/player_list.html', {'players': players})

def player_detail(request, pk):
    """Read - Display single player details"""
    player = get_object_or_404(VolleyballPlayer, pk=pk)
    return render(request, 'players/player_detail.html', {'player': player})

def player_create(request):
    """Create - Add new player"""
    if request.method == 'POST':
        form = VolleyballPlayerForm(request.POST)
        if form.is_valid():
            player = form.save()
            messages.success(request, f'Player {player.name} added successfully!')
            return redirect('player_list')
    else:
        form = VolleyballPlayerForm()
    return render(request, 'players/player_form.html', {'form': form, 'action': 'Create'})

def player_update(request, pk):
    """Update - Edit existing player"""
    player = get_object_or_404(VolleyballPlayer, pk=pk)
    if request.method == 'POST':
        form = VolleyballPlayerForm(request.POST, instance=player)
        if form.is_valid():
            player = form.save()
            messages.success(request, f'Player {player.name} updated successfully!')
            return redirect('player_list')
    else:
        form = VolleyballPlayerForm(instance=player)
    return render(request, 'players/player_form.html', {'form': form, 'action': 'Update'})

def player_delete(request, pk):
    """Delete - Remove player"""
    player = get_object_or_404(VolleyballPlayer, pk=pk)
    if request.method == 'POST':
        player_name = player.name
        player.delete()
        messages.success(request, f'Player {player_name} deleted successfully!')
        return redirect('player_list')
    return render(request, 'players/player_confirm_delete.html', {'player': player})