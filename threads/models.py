from django.contrib.auth.models import User
from django.db import models


class ThreadModel(models.Model):
    title = models.CharField(max_length=20)
    body = models.TextField(max_length=2000)
    game = models.CharField(max_length=30)
    description = models.CharField(max_length=50)
    author = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
