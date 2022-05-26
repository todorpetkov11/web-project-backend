from rest_framework import serializers
from .models import ThreadModel


class ThreadSerializer(serializers.ModelSerializer):
    authorId = serializers.ReadOnlyField(source='author.id')
    author = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = ThreadModel
        fields = ["id", "title", "body", "description", "game", "author", "authorId", "image", "genre"]
