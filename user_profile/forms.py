from django import forms
from .models import MyUser


class ProfileForm(forms.ModelForm):

    class Meta:
        model = MyUser
        fields = ['email', 'first_name', 'last_name']
