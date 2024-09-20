from django.shortcuts import render
from rest_framework import generics

from posts.models import Post
from posts.serializers import PostSerializer


# LIST ALL POSTS VIEW
class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


# CRUD A SINGLE POST VIEW
class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
