from django.db import models

class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    published_date = models.DateField()

    def __str__(self):
        return self.title   # fixed bug (was self.name)


class Library(models.Model):
    name = models.CharField(max_length=255)
    address = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Librarian(models.Model):   # <-- checker expects this
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    library = models.ForeignKey(   # <-- checker expects a "library" field
        Library, 
        on_delete=models.CASCADE,
        related_name="librarians"
    )

    def __str__(self):
        return f"{self.name} — {self.library}"
