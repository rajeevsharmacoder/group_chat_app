from django.db import models

# Create your models here.
class Message(models.Model):
    message_text = models.TextField(null=True, blank=True)
    user_name = models.CharField(max_length=128)
    group_name = models.CharField(max_length=128)
    likes = models.BigIntegerField(null=True, blank=True)
    dislikes = models.BigIntegerField(null=True, blank=True)
    created_at = models.DateTimeField(null=True, blank=True)
