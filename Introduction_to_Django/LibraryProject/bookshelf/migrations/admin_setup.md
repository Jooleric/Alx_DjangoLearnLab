# Django Admin Setup for Book Model

## Steps
1. Registered the Book model in `bookshelf/admin.py`.
2. Created a `BookAdmin` class with:
   - `list_display` to show title, author, publication_year.
   - `search_fields` to search by title and author.
   - `list_filter` to filter by publication year.
3. Ran `python manage.py createsuperuser` to create an admin user.
4. Logged into Django Admin at `http://127.0.0.1:8000/admin`.

## Admin Interface
- Books can be added, updated, and deleted via the admin.
- Table view shows **Title, Author, and Publication Year**.
- Search and filters improve data management.
