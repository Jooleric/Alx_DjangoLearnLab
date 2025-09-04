# CRUD Operations

## Create
>>> from bookshelf.models import Book
>>> book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
>>> book
<Book: 1984 by George Orwell>

## Retrieve
>>> Book.objects.all()
<QuerySet [<Book: 1984 by George Orwell>]>

## Update
>>> book = Book.objects.get(title="1984")
>>> book.title = "Nineteen Eighty-Four"
>>> book.save()
>>> book
<Book: Nineteen Eighty-Four by George Orwell>

## Delete
>>> book.delete()
(1, {'bookshelf.Book': 1})
>>> Book.objects.all()
<QuerySet []>
