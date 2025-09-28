from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import Author, Book
from .serializers import AuthorSerializer, BookSerializer

# CRUD for Books
class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

# CRUD for Authors
class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
