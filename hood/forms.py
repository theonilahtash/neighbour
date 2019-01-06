from django import forms
from .models import Profile, Business, Neighbourhood
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class NewProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user', 'neighbourhood']

class NewBusinessForm(forms.ModelForm):
    class Meta:
        model = Business
        fields =['business_name','business_email','description']
        exclude =['user']

class NewHoodForm(forms.ModelForm):
    class Meta:
        model = Hood
        fields = ['name','location','description']

