from rest_framework import serializers
from .models import ThreadModel


class ThreadSerializer(serializers.ModelSerializer):
    class Meta:
        model = ThreadModel
        fields = ["title", "body", "description", "game", "author"]
