from django.db import models
from django.utils import timezone
# Create your models here.
class Message(models.Model):
    email = models.CharField(max_length=120)
    title = models.CharField(max_length=120)
    message = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title