from django.shortcuts import render,get_object_or_404,redirect
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

def add_book(request):
    if request.method == "POST":

        title = request.POST["title"]
        author = request.POST["author"]
        pages = request.POST["pages"]
        description = request.POST["description"]

        Book.objects.create(
        title=title,
        author=author,
        pages=pages,
        description=description,
    )
        return redirect("home")
    return render(request, "books/add_book.html")

def edit_book(request, book_id):

    book = get_object_or_404(Book, id=book_id)

    if request.method == "POST":

        book.title = request.POST["title"]
        book.author = request.POST["author"]
        book.pages = request.POST["pages"]
        book.description = request.POST["description"]

        book.save()

        return redirect("book_detail", book_id=book.id)

    context = {
        "book": book
    }

    return render(request, "books/edit_book.html", context)

def delete_book(request, book_id):

    book = get_object_or_404(Book, id=book_id)

    if request.method == "POST":
        book.delete()
        return redirect("home")

    return render(
        request,
        "books/delete_book.html",
        {"book": book}
    )
