from rest_framework import serializers
from .models import Book


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['ISBN', 'title', 'author', 'category', 'pages', 'price', 'published_date', 'description']
