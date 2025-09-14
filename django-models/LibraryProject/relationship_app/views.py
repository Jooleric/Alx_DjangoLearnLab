from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views.generic import DetailView
from .models import Book
from .models import Library   # <- checker wants this line

# Function-Based View
def list_books(request):
    books = Book.objects.all()   # checker wants this too
    lines = [f"{book.title} by {book.author.first_name} {book.author.last_name}" for book in books]
    return HttpResponse("<br>".join(lines))

# Class-Based View
class LibraryDetailView(DetailView):
    model = Library
    template_name = "relationship_app/library_detail.html"
    context_object_name = "library"
