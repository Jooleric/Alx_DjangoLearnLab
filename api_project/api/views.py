from rest_framewor import ListAPIView
from rest_framework import generics
from rest_framework import viewsets
from .models import Book
from .serializers import BookSerializer


# ListAPIView
class BookList(ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


# CRUD ViewSet
class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
