from django.urls import path
from .views import author,books,add_books

urlpatterns = [
    path('', author, name='author'),
    path('author/<int:id>/', books, name='books'),
    path('author/add/<int:id>/', add_books, name='add_books'),
    
]