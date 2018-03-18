from django.db import models


class Email(models.Model):
    first_name = models.CharField(max_length=30, min_lenght=3, blank=True)
    last_name = models.CharField(max_length=30,min_lenght=3, blank=True)
    email = models.EmailField(max_length=1200,min_lenght=3, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)



    def email_message(self):
        return self.email

    def email_owner(self):
        return self.first_name, self.last_name


    def email_date(self):
        return self.created_date, self.updated_date


