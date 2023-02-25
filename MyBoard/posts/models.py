from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Post(models.Model):
    """게시글"""
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    title = models.CharField(max_length=128)
    category = models.CharField(max_length=128)
    body = models.TextField(blank=True)
    likes = models.ManyToManyField(User, related_name='like_posts', blank=True)
    published_date = models.DateTimeField(default=timezone.now)
