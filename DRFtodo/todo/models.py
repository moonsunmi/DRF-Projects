from django.db import models


class Todo(models.Model):
    """할 일 하나를 나타내는 클래스"""
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    created_date = models.DateField(auto_now_add=True)
    is_complete = models.BooleanField(default=False)
    is_important = models.BooleanField(default=False)

    def __str__(self):
        """할 일(title)을 반환한다."""
        return self.title
