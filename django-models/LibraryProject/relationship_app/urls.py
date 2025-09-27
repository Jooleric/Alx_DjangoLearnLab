from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_books, name='home'),
    path('books/', views.list_books, name='list_books'),
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),

    # Authentication
    path('register/', views.register, name='register'),
    path('login/', views.LoginView.as_view(template_name="relationship_app/login.html"), name='login'),
    path('logout/', views.LogoutView.as_view(template_name="relationship_app/logout.html"), name='logout'),

    # Role-based views
    path('admin-view/', views.admin_view, name='admin_view'),
    path('librarian-view/', views.librarian_view, name='librarian_view'),
    path('member-view/', views.member_view, name='member_view'),
]
