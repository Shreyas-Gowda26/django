from django.shortcuts import render,get_object_or_404,redirect
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Book
from .forms import BookForm
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import BookSerializer
from rest_framework.decorators import api_view
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import AllowAny
from rest_framework.authentication import BasicAuthentication

@authentication_classes([BasicAuthentication])
@permission_classes([AllowAny])
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

@login_required
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
@login_required
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

@login_required
def delete_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)

    if request.method == "POST":
        book.delete()
        return redirect("home")

    return render(request, "books/delete_book.html", {"book": book})

def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = User.objects.create_user(
            username=username,
            password=password
        )

        login(request, user)  # auto login after register
        return redirect("home")

    return render(request, "books/register.html")

def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            return render(request, "books/login.html", {"error": "Invalid credentials"})

    return render(request, "books/login.html")

def logout_view(request):
    logout(request)
    return redirect("home")

@api_view(['GET', 'POST'])
def book_list_api(request):

    if request.method == 'GET':
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        print("DATA:", request.data)
        serializer = BookSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)

        print(serializer.errors)   # 🔥 ADD THIS
        return Response(serializer.errors, status=400)
    
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from .permissions import IsOwner

class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated, IsOwner]

    filterset_fields = ['author']

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
