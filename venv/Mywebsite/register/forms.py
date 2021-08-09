
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.forms import widgets
from django.forms.widgets import NumberInput, PasswordInput, TextInput


class RegisterForm(UserCreationForm):
    username=forms.CharField(help_text=None,label="نام کاربری")
    password1 = forms.CharField(widget=PasswordInput,label=" گذر واژه ",help_text=None,error_messages='' )
    password2 = forms.CharField(widget=PasswordInput,label="تایید گذر واژه",help_text=None,error_messages='')
    Textarea=forms.TextInput()
    discord_id = forms.CharField(max_length=100, label='شماره تماس ')


    
    class Meta:
        model = User
        fields = ["username", "email","password1","password2","discord_id"]

