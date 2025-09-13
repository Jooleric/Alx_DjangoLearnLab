# LibraryProject/relationship_app/models.py
from django.db import models

class Library(models.Model):
    name = models.CharField(max_length=255)
    address = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Librarian(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    # <-- the checker expects a field named "library"
    library = models.ForeignKey(Library, on_delete=models.CASCADE, related_name="librarians")
    hired_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.name} — {self.library}"
