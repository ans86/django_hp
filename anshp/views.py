from django.http import HttpResponse
from django.shortcuts import render
from game.models import Game
from laptop.models import Laptop
from car.models import Car
from book.models import Book
from author.models import Author



def index(request):
    return render(request, 'gam.html')

def gam_view(request):
#  return HttpResponse("Hello, World!")
     return render(request, 'gam.html')

def home_view(request):
    games = Game.objects.all()
    context = {
        "games": games
    }
    return render(request, 'home.html', context)

def about_view(request):
     return render(request, 'about.html')

def form_view(request):
     return render(request, 'form.html')

def laptops_view(request):
    laptops = Laptop.objects.all()
    context = {
        "laptops": laptops
    }
    return render(request, 'laptops.html', context)

def cars_view(request):
    cars = Car.objects.all()
    context = {
        "cars": cars
    }
    return render(request, 'cars.html', context)

def books_view(request):
    books = Book.objects.all()
    context = {
        "books": books
    }
    return render(request, 'books.html', context)



def authors_view(request):
    authors = Author.objects.all()
    context = {
        "authors": authors
    }
    return render(request, 'authors.html', context)    


