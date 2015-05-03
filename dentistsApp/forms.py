from django.db import models
from django import forms
from .models import Dentist

class DentistForm(forms.Form):
    first_name = forms.CharField(max_length=32)
    last_name = forms.CharField(max_length=32)
    email = forms.CharField(max_length=32)
    license_number = forms.CharField(max_length=64)

class UserForm(forms.Form):
    first_name = forms.CharField(max_length=32)
    last_name = forms.CharField(max_length=32)
    email = forms.CharField(max_length=32)
    dentist = models.ForeignKey(Dentist, default=None)
