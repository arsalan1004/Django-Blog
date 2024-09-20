from rest_framework import serializers

from posts.models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ("id", "title", "author", "body", "created_at")
        model = Post
