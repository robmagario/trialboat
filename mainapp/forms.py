from django import forms
from django.contrib.auth.models import User

from mainapp.models import Customer


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ("address", 'zip', 'city', 'country')
