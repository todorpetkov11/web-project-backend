# Generated by Django 4.0.4 on 2022-06-02 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_customusermodel_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='customusermodel',
            name='image',
            field=models.ImageField(default='media/threads/World_of_Warcraft.png', upload_to=''),
        ),
        migrations.AddField(
            model_name='customusermodel',
            name='username',
            field=models.CharField(default='asd', max_length=20, unique=True),
            preserve_default=False,
        ),
    ]
