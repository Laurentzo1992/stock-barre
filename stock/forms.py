# users/forms.py
from django import forms
from django.core.validators import RegexValidator
from django import forms
from .models import *
from phonenumber_field.widgets import PhoneNumberInternationalFallbackWidget, PhoneNumberPrefixWidget


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
        
        
class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = '__all__'
        widgets = {
            'adresse': forms.Textarea(attrs={'rows': 4, 'cols': 40}),
            'phone_number': PhoneNumberPrefixWidget,
        }
       

        
        
        
class ProductForm(forms.ModelForm):
    code = forms.CharField(widget=forms.TextInput(attrs={'readonly':'readonly'}))
    class Meta:
        model = Product
        fields = '__all__'
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4, 'cols': 40}),
        }
       

class TransporteurForm(forms.ModelForm):
    class Meta:
        model = Transporteur
        fields = '__all__'
        
        widgets = {
            'phone_number': PhoneNumberPrefixWidget,
        }
        
        

class LivraisonForm(forms.ModelForm):
    date_livaison = forms.DateField(
        label='Date de livraison',
        widget=forms.TextInput(attrs={'type': 'date'})
    )
    class Meta:
        model = Livraison
        fields = '__all__'
        
        widgets = {
            'commande': forms.HiddenInput(),
        }
         
         
        
