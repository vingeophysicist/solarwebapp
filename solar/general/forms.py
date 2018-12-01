from django import forms
from django.forms import ModelForm
from .models import contactForms


class contactFormed(forms.ModelForm):
    First_name = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'first name'}))
    Last_name = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Last name'}))
    sender = forms.EmailField(widget=forms.EmailInput(
        attrs={'class': 'form-control', 'placeholder': 'Email'}))

    class Meta:
        model = contactForms
        fields = ('First_name', 'Last_name', 'sender')


"""class contactForms(forms.Form):
    First_name = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'first name'}))
    Last_name = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Last name'}))
    sender = forms.EmailField(widget=forms.EmailInput(
        attrs={'class': 'form-control', 'placeholder': 'Email'}))"""


"""class contactFormed(forms.ModelForm):
    class Meta:
        model = contactForms
        fields = ['First_name', 'Last_name', 'sender']"""
