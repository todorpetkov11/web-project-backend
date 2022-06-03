from rest_framework import serializers
from .models import CommentsModel, LikesModel, AsideModel


class CommentsSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    thread = serializers.ReadOnlyField(source='thread.title')

    class Meta:
        model = CommentsModel
        fields = ["id", "body", "thread", "user"]


class LikesSerializer(serializers.ModelSerializer):
    class Meta:
        model = LikesModel
        fields = ["id", "thread", "user"]


class AsideSerializer(serializers.ModelSerializer):
    class Meta:
        model = AsideModel
        fields = ["id", "type", "body"]
