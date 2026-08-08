from django.shortcuts import render,get_object_or_404,redirect
from .models import Book
from .forms import BookForm
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
        form = BookForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("home")

    else:
        form = BookForm()

    return render(
        request,
        "books/add_book.html",
        {"form": form}
    )

def edit_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)

    if request.method == "POST":
        form = BookForm(request.POST, instance=book)

        if form.is_valid():
            form.save()
            return redirect("book_detail", book_id=book.id)

    else:
        form = BookForm(instance=book)

    return render(request, "books/edit_book.html", {"form": form})

def delete_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)

    if request.method == "POST":
        book.delete()
        return redirect("home")

    return render(request, "books/delete_book.html", {"book": book})
