import datetime

from django.db import models
from django.utils import timezone


class Post(models.Model):
    title = models.CharField(max_length = 100)
    thumbnail = models.ImageField(upload_to = "blog/pictures", blank = True, null = True)
    author = models.CharField(max_length = 12, blank = True, null = True)
    date_posted = models.DateTimeField(default = timezone.now)

    def __str__(self):
        return self.title
        return self.id

class PostContent(models.Model):
    headline = models.CharField(max_length = 20)
    content = models.TextField()
    date_created = models.DateTimeField(default = timezone.now)

    post = models.ForeignKey(Post, null=True, on_delete=models.SET_NULL, related_name = "content")

    def __str__(self):
        return self.headline
