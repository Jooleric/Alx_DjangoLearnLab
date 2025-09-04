# Delete Operation

```python
from bookshelf.models import Book

# Retrieve the book by its title
book = Book.objects.get(title="Nineteen Eighty-Four")

# Delete the book
book.delete()

# Confirm the deletion
Book.objects.all()
# Expected output: <QuerySet []>
