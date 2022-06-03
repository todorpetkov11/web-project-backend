from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView
from users.serializers import UserSerializer, RegisterSerializer
from .models import CustomUserModel
from .serializers import MyTokenObtainPairSerializer
from rest_framework.permissions import AllowAny, IsAuthenticatedOrReadOnly
from rest_framework_simplejwt.views import TokenObtainPairView


class MyObtainTokenPairView(TokenObtainPairView):
    permission_classes = (AllowAny,)
    serializer_class = MyTokenObtainPairSerializer


class RegisterView(CreateAPIView):
    queryset = CustomUserModel.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer


class UsersView(ListCreateAPIView):
    queryset = CustomUserModel.objects.all()
    serializer_class = UserSerializer


class RetrieveUpdateDestroyUserView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = CustomUserModel.objects.all()
    serializer_class = UserSerializer
