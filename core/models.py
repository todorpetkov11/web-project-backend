from django.db import models

from threads.models import ThreadModel
from users.models import CustomUserModel


class CommentsModel(models.Model):
    body = models.TextField(max_length=2000)
    thread = models.ForeignKey(ThreadModel, on_delete=models.CASCADE, related_name='thread_comments')
    user = models.ForeignKey(CustomUserModel, on_delete=models.CASCADE, related_name='user_comments')


class LikesModel(models.Model):
    thread = models.ForeignKey(ThreadModel, on_delete=models.CASCADE, related_name='thread_likes')
    user = models.ForeignKey(CustomUserModel, on_delete=models.CASCADE, related_name='user_likes')


class AsideModel(models.Model):
    type = models.CharField(max_length=10)
    body = models.CharField(max_length=50)
