from django import forms
from .models import Job


class JobForm(forms.ModelForm):

    class Meta:
        model = Job
        fields = ('title', 'email_text',)
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'email_text':forms.Textarea(attrs={'class': 'form-control'})
        }


