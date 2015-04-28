from django.db import models

class User(models.Model):
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    email = models.CharField(max_length=32)
    def  __unicode__(self):
        return (self.first_name + " " + self.last_name)

class Dentist(models.Model):
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    email = models.CharField(max_length=32)
    license_number = models.CharField(max_length=64)
    patients_list = models.ForeignKey(User)
    def  __unicode__(self):
        return (self.first_name + " " + self.last_name)
    def get_license_number(self):
        return self.license_number
