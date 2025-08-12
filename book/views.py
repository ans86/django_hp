from django.shortcuts import render
from book.models import Book

def book(request):
    if request.method=="POST":
        title = request.POST['title']
        image = request.FILES.get('image')
        author = request.POST['author']
        publishyear = request.POST['publishyear']
        book = Book(title=title, image=image, author=author, publishyear=publishyear)
        book .save()   
    return render(request, "book_form.html")