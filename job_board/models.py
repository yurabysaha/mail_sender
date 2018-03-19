from django.db import models
from django.contrib.auth.models import User


class Job(models.Model):
    user = models.ForeignKey('auth.User', on_delete = models.CASCADE)
    title = models.CharField(max_length=18)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    email_text = models.TextField()

    def get_title(self):
        return self.title

    def get_email_text(self):
        return self.email_text
