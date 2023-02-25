from rest_framework import serializers
from .models import Todo


class TodoSimpleSerializer(serializers.ModelSerializer):
    """투두 전체 조회용 시리얼라이저 클래스.
    제목(title), 완료 여부(is_complete), 중요 여부(is_important)"""
    class Meta:
        model = Todo
        fields = ('id', 'title', 'is_complete', 'is_important')


class TodoDetailSerializer(serializers.ModelSerializer):
    """투두 하나의 모든 정보를 조회하는 시리얼라이저 클래스."""
    class Meta:
        model = Todo
        fields = ('id', 'title', 'description', 'created_date', 'is_complete', 'is_important')


class TodoCreateSerializer(serializers.ModelSerializer):
    """투두 하나를 만드는 시리얼라이저 클래스."""
    class Meta:
        model = Todo
        fields = ('id', 'title', 'description', 'is_important')
