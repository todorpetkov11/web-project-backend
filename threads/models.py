import os

from django.contrib.auth.models import User
from django.db import models
from django.dispatch import receiver


class ThreadModel(models.Model):
    title = models.CharField(max_length=20)
    body = models.TextField(max_length=2000)
    game = models.CharField(max_length=30)
    description = models.CharField(max_length=50)
    image = models.ImageField(upload_to='threads/')
    author = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)


@receiver(models.signals.post_delete, sender=ThreadModel)
def remove_image_on_delete(sender, instance, **kwargs):
    if instance.image:
        if os.path.isfile(instance.image.path):
            os.remove(instance.image.path)


@receiver(models.signals.pre_save, sender=ThreadModel)
def remove_image_on_change(sender, instance, **kwargs):
    if not instance.pk:
        return False

    try:
        old_file = ThreadModel.objects.get(pk=instance.pk).image
    except ThreadModel.DoesNotExist:
        return False

    new_file = instance.image
    if not old_file == new_file:
        if os.path.isfile(old_file.path):
            os.remove(old_file.path)