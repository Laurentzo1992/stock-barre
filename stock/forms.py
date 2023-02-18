# users/forms.py
from django import forms
from django.core.validators import RegexValidator
from django import forms
from .models import *

class LoginForm(forms.Form):
    username = forms.CharField(max_length=63, label='Nom tilisateur')
    password = forms.CharField(max_length=63, widget=forms.PasswordInput, label='Mot de passe')
    
 

class Niveau1Form(forms.ModelForm):
    class Meta:
        model = Niveau1
        fields = '__all__'
        
        
        
class Niveau2Form(forms.ModelForm):
    class Meta:
        model = Niveau2
        fields = '__all__'
        


        

class Niveau3Form(forms.ModelForm):
    class Meta:
        model = Niveau3
        fields = '__all__'
        
        

class Niveau4Form(forms.ModelForm):
    class Meta:
        model = Niveau4
        fields = '__all__'
        
        
        
class Niveau5Form(forms.ModelForm):
    class Meta:
        model = Niveau5
        fields = '__all__'
        
        
        
class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4, 'cols': 40}),
        }