from django.contrib.auth.models import User
from rest_framework import serializers

from threads.models import ThreadModel


class UserSerializer(serializers.ModelSerializer):
    threads = serializers.PrimaryKeyRelatedField(many=True, queryset=ThreadModel.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username', 'threads']
