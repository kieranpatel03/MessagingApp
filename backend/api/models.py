from django.db import models

# Create your models here.
class Message(models.Model):
    user_sent = models.IntegerField()
    user_to = models.IntegerField()
    message = models.CharField(max_length = 1000)
    date_sent = models.DateField()
    message_read = models.BooleanField()
