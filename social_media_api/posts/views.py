from rest_framework import viewsets, permissions, filters
from rest_framework.response import Response
from rest_framework.decorators import action
from django.db.models import Q

from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer


# --- Custom Permission ---
class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to allow only post/comment owners to edit or delete.
    Others can only read.
    """
    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed for any request
        if request.method in permissions.SAFE_METHODS:
            return True
        # Write permissions only for the owner
        return obj.author == request.user


# --- Post ViewSet ---
class PostViewSet(viewsets.ModelViewSet):
    """
    Provides CRUD operations for posts.
    """
    queryset = Post.objects.all().order_by('-created_at')
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'content', 'author__username']

    def perform_create(self, serializer):
        # Automatically assign the logged-in user as the post author
        serializer.save(author=self.request.user)

    @action(detail=False, methods=['get'], permission_classes=[permissions.IsAuthenticated])
    def feed(self, request):
        """
        Custom action: Returns posts from users the authenticated user follows.
        """
        user = request.user
        following_users = user.following.all()  # users the current user follows
        posts = Post.objects.filter(author__in=following_users).order_by('-created_at')
        serializer = self.get_serializer(posts, many=True)
        return Response(serializer.data)


# --- Comment ViewSet ---
class CommentViewSet(viewsets.ModelViewSet):
    """
    Provides CRUD operations for comments.
    """
    queryset = Comment.objects.all().order_by('-created_at')
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        # Automatically assign the logged-in user as the comment author
        serializer.save(author=self.request.user)
