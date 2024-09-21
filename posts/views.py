from django.shortcuts import render
from rest_framework import generics, permissions

from accounts.models import User
from posts.models import Post
from posts.serializers import PostSerializer, UserSerializer


# LIST ALL POSTS VIEW
class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


# CRUD A SINGLE POST VIEW
class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class UserList(generics.ListCreateAPIView):
    permission_classes = permissions.IsAdminUser
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = permissions.IsAdminUser
    queryset = User.objects.all()
    serializer_class = UserSerializer
