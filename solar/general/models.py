from django.db import models
from django.forms import ModelForm


# Create your models here.


"""class Name(models.Model):
    First_name = models.CharField(max_length=30)
    Last_name = models.CharField(max_length=30)
    sender = models.EmailField()

    def __str__(self):
        return self.first_name


class contactForms(ModelForm):
    class Meta:
        model = Name
        fields = ['First_name', 'Last_name', 'Email']"""


class contactForms(models.Model):
    First_name = models.CharField(max_length=30)
    Last_name = models.CharField(max_length=30)
    sender = models.EmailField()
