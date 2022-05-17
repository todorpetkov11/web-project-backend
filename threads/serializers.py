from rest_framework import serializers
from .models import ThreadModel


class ThreadSerializer(serializers.ModelSerializer):

    author = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = ThreadModel
        fields = ["id", "title", "body", "description", "game", "author", "image", "genre"]
