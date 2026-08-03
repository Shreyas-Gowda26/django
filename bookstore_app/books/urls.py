from django.urls import path

from books import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:book_id>/', views.book_detail, name='book_detail'),
]
