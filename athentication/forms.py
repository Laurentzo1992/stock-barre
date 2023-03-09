# users/forms.py
from django import forms
from django.core.validators import RegexValidator
from django import forms
from .models import *
from phonenumber_field.widgets import PhoneNumberInternationalFallbackWidget, PhoneNumberPrefixWidget


class LoginForm(forms.Form):
    username = forms.CharField(max_length=63, label='Nom tilisateur')
    password = forms.CharField(max_length=63, widget=forms.PasswordInput, label='Mot de passe')
    
 