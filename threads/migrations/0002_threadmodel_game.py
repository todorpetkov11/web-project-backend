# Generated by Django 4.0.4 on 2022-05-11 19:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('threads', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='threadmodel',
            name='game',
            field=models.CharField(default='World of Warcraft', max_length=30),
            preserve_default=False,
        ),
    ]
