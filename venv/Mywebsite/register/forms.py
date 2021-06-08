from typing import Hashable, Text
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class RegisterForm(UserCreationForm):
    email = forms.EmailField()
    #username=forms.CharField(help_text=None)
    password2=forms.PasswordInput()
    
    class Meta:
        model = User
        fields = ["username", "password1", "password2", "email"]

