from django.contrib.auth.models import User
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from users.serializers import UserSerializer


class UsersView(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class RetrieveUser(RetrieveUpdateDestroyAPIView):
    lookup_field = "username"
    queryset = User.objects.all()
    serializer_class = UserSerializer
