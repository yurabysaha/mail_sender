from django.db import models
from django.contrib.auth.models import User

from mail_sender import settings


class Job(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=18)
    from_email_send = models.EmailField()
    delay_time = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    email_text = models.TextField()

    def get_title(self):
        return self.title

    def get_email_text(self):
        return self.email_text
