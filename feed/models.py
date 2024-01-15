from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class tweet(models.Model):
    text = models.TextField(max_length=280, default='')
    datetime = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    #likes = models.ManyToManyField(User, related_name="tweet_likes", blank=True)

    #def number_of_likes(self):
        #return self.likes.count()
