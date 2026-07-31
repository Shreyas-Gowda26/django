from django.shortcuts import render,get_object_or_404
from .models import Book
# Create your views here.
def home(request):
    books = Book.objects.all()

    context = {
        'books': books
    }
    return render(request, 'books/index.html', context)

def book_detail(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    context = {
        'book': book
    }
    return render(request, 'books/detail.html', context)

from django.shortcuts import render, redirect
from .models import Book

def add_book(request):
    if request.method == "POST":

        title = request.POST["title"]
        author = request.POST["author"]
        pages = request.POST["pages"]
        description = request.POST["description"]

        print(title)
        print(author)

    return render(request, "books/add_book.html")