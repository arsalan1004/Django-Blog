from rest_framework import serializers

from accounts.models import User
from posts.models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ("id", "title", "author", "body", "created_at")
        model = Post


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("name",)
