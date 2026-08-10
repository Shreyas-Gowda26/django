from django.urls import path, include
from books import views
from rest_framework.routers import DefaultRouter
from .views import BookViewSet

# 🔥 Router
router = DefaultRouter()
router.register('api/books', BookViewSet)

# ✅ KEEP your normal views
urlpatterns = [
    path('', views.home, name='home'),
    path('<int:book_id>/', views.book_detail, name='book_detail'),
    path('add/', views.add_book, name='add_book'),
    path('<int:book_id>/edit/', views.edit_book, name='edit_book'),
    path('<int:book_id>/delete/', views.delete_book, name='delete_book'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]

# ✅ ADD router URLs (DON’T overwrite)
urlpatterns += router.urls


