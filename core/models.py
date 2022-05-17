from django.contrib.auth.models import User
from django.db import models

from threads.models import ThreadModel


class CommentsModel(models.Model):
    body = models.TextField(max_length=2000)
    thread = models.ForeignKey(ThreadModel, on_delete=models.CASCADE, related_name='thread_comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_comments')


class LikesModel(models.Model):
    thread = models.ForeignKey(ThreadModel, on_delete=models.CASCADE, related_name='thread_likes')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_likes')
