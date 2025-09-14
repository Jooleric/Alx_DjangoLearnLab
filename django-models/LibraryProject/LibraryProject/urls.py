"""
URL configuration for LibraryProject project.
"""

from django.contrib import admin
from django.urls import path, include   # include is needed to hook app urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('relationship_app.urls')),  # include app routes
]
