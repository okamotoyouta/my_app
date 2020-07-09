import datetime

from django.db import models
from django.utils import timezone


class Update(models.Model):
    title = models.CharField(max_length = 100)
    date_posted = models.DateTimeField(default = timezone.now)

    def __str__(self):
        return self.title

    def new(self):
        return self.date_posted > (timezone.now() - datetime.timedelta(days = 3))

class UpdateDetail(models.Model):
    headline = models.CharField(max_length = 20)
    content = models.TextField()

    detail = models.ForeignKey(Update, null=True, on_delete=models.SET_NULL, related_name = "content")

    def __str__(self):
        return self.headline
