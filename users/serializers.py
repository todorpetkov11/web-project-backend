from django.contrib.auth.models import User
from rest_framework import serializers

from core.models import CommentsModel, LikesModel
from threads.models import ThreadModel


class UserSerializer(serializers.ModelSerializer):
    threads = serializers.PrimaryKeyRelatedField(many=True, queryset=ThreadModel.objects.all())
    user_comments = serializers.PrimaryKeyRelatedField(many=True, queryset=CommentsModel.objects.all())
    user_likes = serializers.PrimaryKeyRelatedField(many=True, queryset=LikesModel.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username', 'threads', 'user_comments', 'user_likes', ]
