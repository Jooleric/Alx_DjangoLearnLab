from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)       # book title
    author = models.CharField(max_length=100)      # book author
    publication_year = models.IntegerField()       # year of publication

    def __str__(self):
        return f"{self.title} by {self.author}"
