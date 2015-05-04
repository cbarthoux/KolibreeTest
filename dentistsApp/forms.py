from django.db import models
from django import forms
from .models import Dentist, User

class DentistForm(forms.Form):
    first_name = forms.CharField(max_length=32, label='')
    last_name = forms.CharField(max_length=32, label='')
    email = forms.CharField(max_length=32, label='')
    license_number = forms.CharField(max_length=64, label='')
    def __init__(self, *args, **kwargs):
        super(DentistForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs['class'] = 'form-control'
        self.fields['last_name'].widget.attrs['class'] = 'form-control'
        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['license_number'].widget.attrs['class'] = 'form-control'
        self.fields['first_name'].widget.attrs['placeholder'] = 'First name'
        self.fields['last_name'].widget.attrs['placeholder'] = 'Last name'
        self.fields['email'].widget.attrs['placeholder'] = 'Email'
        self.fields['license_number'].widget.attrs['placeholder'] = 'License number'

class UserForm(forms.Form):
    first_name = forms.CharField(max_length=32, label='')
    last_name = forms.CharField(max_length=32, label='')
    email = forms.CharField(max_length=32, label='')
    dentist = forms.ModelChoiceField(queryset=Dentist.objects.all(), required=False)
    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs['class'] = 'form-control'
        self.fields['last_name'].widget.attrs['class'] = 'form-control'
        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['dentist'].widget.attrs['class'] = 'form-control'
        self.fields['first_name'].widget.attrs['placeholder'] = 'First name'
        self.fields['last_name'].widget.attrs['placeholder'] = 'Last name'
        self.fields['email'].widget.attrs['placeholder'] = 'Email'

class MatchForm(forms.Form):
    user = forms.ModelChoiceField(queryset=User.objects.all())
    dentist = forms.ModelChoiceField(queryset=Dentist.objects.all())
    def __init__(self, *args, **kwargs):
        super(MatchForm, self).__init__(*args, **kwargs)
        self.fields['user'].widget.attrs['class'] = 'form-control'
        self.fields['dentist'].widget.attrs['class'] = 'form-control'
