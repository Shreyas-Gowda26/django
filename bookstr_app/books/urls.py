from django.urls import path
from books import views

urlpatterns = [
    path('', views.home, name='home'),
    path('<int:book_id>/', views.book_detail, name='book_detail'),
    path('add/', views.add_book, name='add_book')
]