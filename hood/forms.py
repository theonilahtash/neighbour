from django import forms
from .models import Profile, Business
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class NewProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user', 'email']

class BusinessForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['name','user','hood']

