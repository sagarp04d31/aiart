# Generated by Django 4.1 on 2023-07-03 08:52

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0002_alter_profile_followers'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='followers',
        ),
        migrations.AddField(
            model_name='profile',
            name='follow',
            field=models.ManyToManyField(blank=True, null=True, related_name='follow', to=settings.AUTH_USER_MODEL),
        ),
    ]
