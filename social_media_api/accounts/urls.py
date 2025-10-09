from django.urls import path
from rest_framework import routers
from .views import FollowUserView, UnfollowUserView

app_name = "accounts"

urlpatterns = [
    path('follow/<int:pk>/', FollowUserView.as_view(), name='follow-user'),
    path('unfollow/<int:pk>/', UnfollowUserView.as_view(), name='unfollow-user'),
]
