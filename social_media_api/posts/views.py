from rest_framework import viewsets, permissions, filters, status
from rest_framework.response import Response
from rest_framework.decorators import action
from django.shortcuts import get_object_or_404
from django.db.models import Q

from .models import Post, Comment, Like
from .serializers import PostSerializer, CommentSerializer
from notifications.models import Notification


# --- Custom Permission ---
class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission: only owners can edit/delete.
    """
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.author == request.user


# --- Post ViewSet ---
class PostViewSet(viewsets.ModelViewSet):
    """
    Provides CRUD operations for posts + like/unlike functionality.
    """
    queryset = Post.objects.all().order_by('-created_at')
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'content', 'author__username']

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    @action(detail=False, methods=['get'], permission_classes=[permissions.IsAuthenticated])
    def feed(self, request):
        """
        Returns posts from users the authenticated user follows.
        """
        user = request.user
        following_users = user.following.all()
        posts = Post.objects.filter(author__in=following_users).order_by('-created_at')
        serializer = self.get_serializer(posts, many=True)
        return Response(serializer.data)

    # ✅ LIKE a Post
    @action(detail=True, methods=['post'], permission_classes=[permissions.IsAuthenticated])
    def like(self, request, pk=None):
        """
        Allows a user to like a post (if not already liked).
        """
        post = get_object_or_404(Post, pk=pk)
        user = request.user

        like, created = Like.objects.get_or_create(post=post, user=user)

        if not created:
            return Response({'detail': 'You have already liked this post.'}, status=status.HTTP_400_BAD_REQUEST)

        # Create a notification for the post author
        if post.author != user:
            Notification.objects.create(
                recipient=post.author,
                actor=user,
                verb="liked your post",
                target=post
            )

        return Response({'detail': 'Post liked successfully.'}, status=status.HTTP_201_CREATED)

    # ✅ UNLIKE a Post
    @action(detail=True, methods=['post'], permission_classes=[permissions.IsAuthenticated])
    def unlike(self, request, pk=None):
        """
        Allows a user to unlike a post they previously liked.
        """
        post = get_object_or_404(Post, pk=pk)
        user = request.user

        like = Like.objects.filter(post=post, user=user)
        if not like.exists():
            return Response({'detail': 'You have not liked this post yet.'}, status=status.HTTP_400_BAD_REQUEST)

        like.delete()
        return Response({'detail': 'Post unliked successfully.'}, status=status.HTTP_200_OK)


# --- Comment ViewSet ---
class CommentViewSet(viewsets.ModelViewSet):
    """
    Provides CRUD operations for comments.
    """
    queryset = Comment.objects.all().order_by('-created_at')
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        comment = serializer.save(author=self.request.user)

        # Notify post author when a new comment is made
        post = comment.post
        if post.author != self.request.user:
            Notification.objects.create(
                recipient=post.author,
                actor=self.request.user,
                verb="commented on your post",
                target=post
            )
