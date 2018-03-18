from django.db import models


class Email(models.Model):
    first_name = models.CharField(max_length=30, min_lenght=3)
    last_name = models.CharField(max_length=30, blank=True)
    email = models.EmailField(min_lenght=3)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)



