from django import forms
from email_service.models import Email
from .models import Job


class JobForm(forms.ModelForm):

    class Meta:
        model = Job
        fields = ('title', 'email_text',)
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'email_text':forms.Textarea(attrs={'class': 'form-control'})
        }

class AddEmailForm(forms.ModelForm):

    class Meta:
        model = Email
        fields = ('email', 'first_name',)
        widgets = {
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'})
        }