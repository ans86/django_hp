from django.shortcuts import render, HttpResponse
from game.models import Game

def game(request):
    if request.method == "POST":
        name = request.POST.get('name')
        image = request.FILES.get('image')
        message = request.POST.get('message')


        game_obj = Game(name=name, image=image, message=message)
        game_obj.save()

    return render(request, 'game.html')


def game_list(request):
    games=Game.objects.all()
    return render(request, 'home.html',games=games)