from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    gender = forms.CharField(max_length=1)

    class Meta:
        model = User
        fields = ['username', 'email', 'gender','password1', 'password2']
