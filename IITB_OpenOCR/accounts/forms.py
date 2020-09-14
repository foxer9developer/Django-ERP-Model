from django.forms import ModelForm
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from IIT_OpenOCR.models import users


class RegisterationForm(ModelForm):
    class Meta:
        model = users
        fields = ['github_username', 'user_role', 'name', 'user_email']


class loginForm():
    class Meta:
        model = User
        fields = []