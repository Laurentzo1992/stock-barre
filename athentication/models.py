from django.contrib.auth.models import AbstractUser
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

class User(AbstractUser):
    
    phone_number = PhoneNumberField(unique=True, null=True, blank=True, verbose_name="Numero de téléphone")
   
    