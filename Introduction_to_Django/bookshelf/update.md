# Update Operation

```python
from bookshelf.models import Book

# Retrieve the book by its title
book = Book.objects.get(title="1984")

# Update the title
book.title = "Nineteen Eighty-Four"
book.save()

# Confirm the update
book.title
# Expected output: 'Nineteen Eighty-Four'
