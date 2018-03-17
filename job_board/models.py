from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Job (models.Model):

    user = models.ForeignKey('auth.User', on_delete = models.CASCADE)
    title = models.CharField(max_length=18)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(blank=True, null=True)
    email_text = models.TextField()

    def updated(self):
        self.updated_at = timezone.now()
        self.save()

    def get_title(self):
        return self.title

    def get_email_text(self):
        return self.email_text






