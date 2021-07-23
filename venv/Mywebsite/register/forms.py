
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.forms import widgets
from django.forms.widgets import NumberInput, TextInput


class RegisterForm(UserCreationForm):
    email = forms.EmailField()
    #username=forms.CharField(help_text=None)
    password2=forms.PasswordInput()
    Textarea=forms.TextInput()
    
    
    class Meta:
        model = User
        fields = ["username", "password1", "password2", "email"]

