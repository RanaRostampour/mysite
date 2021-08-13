
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.forms import widgets
from django.forms.widgets import NumberInput, PasswordInput, TextInput


class RegisterForm(UserCreationForm):
    courses= {
    ('LPIC1', 'LPIC1'),
    ('LPIC2', 'LPIC2'),
    ('network+', '+NETWORK'),
    ('DOCKER', 'DOCKER'),
    ('Laravel','Laravel'),
    ('PHP','PHP'),
    ('Git & Jenkins','Git & Jenkins'),
    ('Puppet','Puppet'),
    ('SaltStack','SaltStack')
    }
    
    username=forms.CharField(help_text=None,label="نام کاربری")
    password1 = forms.CharField(widget=PasswordInput,label=" گذر واژه ",help_text=None,error_messages='' )
    password2 = forms.CharField(widget=PasswordInput,label="تایید گذر واژه",help_text=None,error_messages='')
    Textarea=forms.TextInput()
    discord_id = forms.IntegerField( label='شماره تماس ')
    widget=forms.MultipleChoiceField(
        label="دوره ها",
        required=False,
        widget=forms.CheckboxSelectMultiple,
        choices=courses
    )

    
    class Meta:
        model = User
        fields = ["widget","username", "email","password1","password2","discord_id"]

