from django.db import models
from django.contrib.auth.models import AbstractUser

from .managers import CustomUserManager


class CustomUserModel(AbstractUser):
    username = models.CharField(unique=True, max_length=20)
    email = models.EmailField('email address', unique=True)
    image = models.ImageField(default='media/threads/World_of_Warcraft.png')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = CustomUserManager()

    spouse_name = models.CharField(blank=True, max_length=100)
    date_of_birth = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.email
