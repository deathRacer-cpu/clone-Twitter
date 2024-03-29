# Generated by Django 4.2.4 on 2023-08-16 07:18

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('feed', '0002_alter_tweet_text'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tweet',
            old_name='uname',
            new_name='user',
        ),
        migrations.AddField(
            model_name='tweet',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='tweet_likes', to=settings.AUTH_USER_MODEL),
        ),
    ]
