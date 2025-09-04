from django.contrib import admin
from .models import Book

# Customizing how Book is displayed in the admin
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')  # show these fields in list view
    search_fields = ('title', 'author')  # enable search by title and author
    list_filter = ('publication_year',)  # add filter on publication year

# Register the model with the custom admin class
admin.site.register(Book, BookAdmin)
