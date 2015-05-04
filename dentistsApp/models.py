from django.db import models
from django.forms import ModelForm

class Dentist(models.Model):
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    email = models.CharField(max_length=32)
    license_number = models.CharField(max_length=64)
    def  __unicode__(self):
        return (self.first_name + " " + self.last_name)
    def get_license_number(self):
        return self.license_number

class User(models.Model):
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    email = models.CharField(max_length=32)
    dentist = models.ForeignKey(Dentist, null=True)
    def  __unicode__(self):
        return (self.first_name + " " + self.last_name)

class DentistForm(ModelForm):
    class Meta:
        model = Dentist
        fields = ['first_name', 'last_name', 'email', 'license_number']

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'dentist']
