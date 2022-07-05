from django.shortcuts import render, redirect

from GamesPlayApp.web.forms import CreateProfileForm, CreateGameForm, EditGameForm, DeleteGameForm, EditProfileForm, \
    DeleteProfileForm
from GamesPlayApp.web.models import Profile, Game


def get_profile():
    profiles = Profile.objects.all()
    if profiles:
        return profiles[0]
    return None


def show_index(request):
    profile = get_profile()
    if profile:
        context = {
            'profile': True,
        }
    else:
        context = {
            'profile': False
        }
    return render(request, 'home-page.html', context)


def create_profile(request):
    if request.method == 'POST':
        form = CreateProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show index')
    form = CreateProfileForm
    context = {
        'form': form,
    }

    return render(request, 'create-profile.html', context)


def dashboard(request):
    profile = get_profile()
    games = Game.objects.all()

    context = {
        'profile': profile,
        'games': games,
    }
    return render(request, 'dashboard.html', context)


def create_game(request):
    profile = get_profile()
    if request.method == 'POST':
        form = CreateGameForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = CreateGameForm()

    context = {
        'profile': profile,
        'form': form
    }
    return render(request, 'create-game.html', context)


def details_game(request, pk):
    game = Game.objects.get(pk=pk)
    profile = get_profile()

    context = {
        'game': game,
        'profile': profile,
    }
    return render(request, 'details-game.html', context)


def edit_game(request, pk):
    game = Game.objects.get(pk=pk)
    profile = get_profile()
    if request.method == 'POST':
        form = EditGameForm(request.POST, instance=game)
        if form.is_valid():
            form.save()
            return redirect('show index')
    else:
        form = EditGameForm(instance=game)

    context = {
        'form': form,
        'game': game,
        'profile': profile,
    }
    return render(request, 'edit-game.html', context)


def delete_game(request, pk):
    game = Game.objects.get(pk=pk)
    profile = get_profile()
    if request.method == 'POST':
        form = DeleteGameForm(request.POST, instance=game)
        if form.is_valid():
            form.save()
            return redirect('show index')
    else:
        form = DeleteGameForm(instance=game)

    context = {
        'form': form,
        'game': game,
        'profile': profile,
    }
    return render(request, 'delete-game.html', context)


def details_profile(request):
    average_rating = 0
    profile = get_profile()
    games = Game.objects.all()
    game_count = len(games)
    if game_count > 0:
        average_rating = sum(g.rating for g in games) / len(games)
    context = {
        'profile': profile,
        'games': games,
        'average_rating': average_rating,
        'game_count': game_count,
    }
    return render(request, 'details-profile.html', context)


def edit_profile(request):
    profile = get_profile()
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('show index')
    form = EditProfileForm(instance=profile)
    context = {
        'profile': profile,
        'form': form,
    }
    return render(request, 'edit-profile.html', context)


def delete_profile(request):
    profile = get_profile()
    if request.method == 'POST':
        form = DeleteProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('show index')
    form = DeleteProfileForm(instance=profile)
    context = {
        'profile': profile,
        'form': form,
    }
    return render(request, 'delete-profile.html', context)
