from rest_framework import serializers
from .models import Post


class PostCreateSerializer(serializers.ModelSerializer):
    """게시글에서 사용자에게 입력 받는 부분의 시리얼라이저.
    유저가 입력한 데이터를 검증하고, 이를 Django 데이터로 변환하여 저장한다."""

    class Meta:
        model = Post
        fields = ('title', 'category', 'body', 'image')


class PostSerializer(serializers.ModelSerializer):
    """포스트의 모든 정보를 json으로 전달하는 시리얼라이저."""

    class Meta:
        model = Post
        fields = ('author', 'title', 'category', 'body', 'image', 'likes', 'published_date')
