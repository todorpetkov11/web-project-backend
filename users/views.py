from django.contrib.auth.models import User
from rest_framework.generics import ListCreateAPIView, RetrieveAPIView
from users.serializers import UserSerializer


class UsersView(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class RetrieveUser(RetrieveAPIView):
    lookup_field = "username"
    queryset = User.objects.all()
    serializer_class = UserSerializer
