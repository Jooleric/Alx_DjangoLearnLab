from django.urls import path
from .views import list_books, LibraryDetailView, register, login_view, logout_view

urlpatterns = [
    path('', list_books, name='home'),  # or your homepage view
    path('books/', list_books, name='list_books'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
    
    # Authentication
    path('register/', register, name='register'),  # 👈 fix here
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
]

