from django.db import models

# Create your models here.
from django.db import models
from django.core.exceptions import ValidationError
from datetime import date

# Author model represents an author of books
class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


# Book model represents a book written by an author
class Book(models.Model):
    title = models.CharField(max_length=200)
    publication_year = models.IntegerField()
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title} ({self.publication_year})"

    # Custom validation to ensure publication year is not in the future
    def clean(self):
        if self.publication_year > date.today().year:
            raise ValidationError("Publication year cannot be in the future.")
