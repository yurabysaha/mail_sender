from django import forms
from .models import MyUser


class ProfileForm(forms.ModelForm):

    class Meta:
        model = MyUser
        fields = ['email', 'first_name', 'last_name']
        widgets = {
                'email': forms.EmailInput(attrs={'class': 'form-control' }),
                'first_name':forms.TextInput(attrs={'class': 'form-control'}),
                'last_name':forms.TextInput(attrs={'class': 'form-control'})

            }

class RegisterForm(forms.ModelForm):

    class Meta:
        model = MyUser
        fields = ['email', 'first_name', 'last_name', 'password']
        widgets = {
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'password': forms.TextInput(attrs={'class': 'form-control'})
        }
