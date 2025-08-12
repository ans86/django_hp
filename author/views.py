from django.shortcuts import render , HttpResponse, redirect, get_object_or_404
from author.models import Author, Books

def author(request):
    if request.method=="POST":
        name = request.POST['name']
        image = request.FILES.get('image')
        fathername = request.POST['fathername']
        publishedbooks = request.POST['publishedbooks']
        author = Author(name=name, image=image, fathername=fathername, publishedbooks=publishedbooks)
        author .save()   
    return render(request, "author_form.html")


def books(request, id):
    author = get_object_or_404(Author, id=id)
    books = Books.objects.filter(author=author)  # Author ki saari books
    return render(request, 'book.html', {
        'author': author,
        'books': books
    })




def add_books(request, id):
    author = get_object_or_404(Author, id=id)
    
    if request.method == "POST":
        title = request.POST['title']
        image = request.FILES.get('image')
        publishyear = request.POST['publishyear']

        Books.objects.create(
            title=title,
            image=image,
            author=author,
            publishyear=publishyear,
        )
        return redirect('books', id=author.id)

    return render(request, 'add_books.html', {'author': author})