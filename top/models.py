import datetime

from django.db import models
from django.utils import timezone


class Topics(models.Model):
    title = models.CharField(max_length = 100)
    topic = models.TextField()
    date_topiced = models.DateTimeField(default = timezone.now)
    def __str__(self):
        return self.title
        return self.id
