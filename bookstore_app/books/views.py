from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
import json
from books.models import Book

# Create your views here.
booksData = open(
    '/Users/shreyasg/Desktop/DJANGO_PRACTICE/bookstore_app/books.json'
).read()



def index(request):
    dbData = Book.objects.all()
    context = {
        'books': dbData,
    }
    return render(request, 'books/index.html',context)

def book_detail(request, book_id):
    singleBook = get_object_or_404(Book, id=book_id)
    context = {
        'book': singleBook,
    }
    return render(request, 'books/show.html', context)