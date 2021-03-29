from django.db import models

# Create your models here.


class Message(models.Model):
    email = models.EmailField(help_text="Author email")
    text = models.CharField(
        max_length=99, blank=False, null=False, help_text="chat message"
    )
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
