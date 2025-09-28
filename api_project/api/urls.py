from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookList, BookViewSet

# ✅ Router for CRUD ViewSet
router = DefaultRouter()
router.register(r'books_all', BookViewSet, basename='book_all')

urlpatterns = [
    # URL for BookList
    path('books/', BookList.as_view(), name='book-list'),

    # ✅ Include router URLs for CRUD
    path('', include(router.urls)),
]
