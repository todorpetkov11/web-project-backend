# Generated by Django 4.0.4 on 2022-05-17 21:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('threads', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='threadmodel',
            name='genre',
            field=models.CharField(default='MOBA', max_length=10),
            preserve_default=False,
        ),
    ]
