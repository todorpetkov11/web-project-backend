from users.models import CustomUserModel
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from core.models import CommentsModel, LikesModel
from threads.models import ThreadModel


class UserSerializer(serializers.ModelSerializer):
    threads = serializers.PrimaryKeyRelatedField(many=True, queryset=ThreadModel.objects.all())
    user_comments = serializers.PrimaryKeyRelatedField(many=True, queryset=CommentsModel.objects.all())
    user_likes = serializers.PrimaryKeyRelatedField(many=True, queryset=LikesModel.objects.all())

    class Meta:
        model = CustomUserModel
        fields = ['id', 'username', 'threads', 'user_comments', 'user_likes', 'image', 'is_staff', 'email']
        read_only_fields = ('email',)


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super(MyTokenObtainPairSerializer, cls).get_token(user)
        token['username'] = user.username
        return token


class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=CustomUserModel.objects.all())]
    )
    username = serializers.CharField(max_length=20, required=True)
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)
    image = serializers.ImageField()

    class Meta:
        model = CustomUserModel
        fields = ('username', 'password', 'password2', 'email', 'image')

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})

        return attrs

    def create(self, validated_data):
        user = CustomUserModel.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            image=validated_data['image']
        )

        user.set_password(validated_data['password'])
        user.save()

        return user
