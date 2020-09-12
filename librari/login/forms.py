from django import forms
from django.contrib.auth.models import User
from django.core.validators import validate_email
from django.contrib.auth.hashers import make_password,check_password

import re

class UserLoginForm(forms.Form):
    username = forms.CharField(max_length=30)
    password = forms.CharField(max_length=254,widget=forms.PasswordInput())
    fields = ['username', 'password']
    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs \
            .update({
            'placeholder': 'Username or email',
            'class': 'input100'
        })
        self.fields['password'].widget.attrs \
            .update({
            'placeholder': 'Password',
            'class': 'input100'
        })
    def clean(self):
        cleaned_data = super().clean()


class UserSignupForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password',
        ]
        widgets = {
            'password': forms.PasswordInput()
        }

    def __init__(self, *args, **kwargs):
        super(UserSignupForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs \
            .update({
            'placeholder': 'Username',
            'class': 'input100'
        })
        self.fields['email'].widget.attrs \
            .update({
            'placeholder': 'Email',
            'class': 'input100'
        })
        self.fields['password'].widget.attrs \
            .update({
            'placeholder': 'Password',
            'class': 'input100'
        })

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get("username")
        email = cleaned_data.get("email")
        password = cleaned_data.get("password")

        if len(username) < 4:
            self.add_error("username","Username must be at least 4 characters long")
        elif len(username) > 30:
            self.add_error("username","Username cannot be longer than 30 characters")
        elif not re.match("[a-zA-Z]\w{3,29}",username):
            self.add_error("username","The username can only contain alphanumeric characters and underscores (_)")

        if len(email) > 254:
            self.add_error("email","Email cannot be longer than 254 characters")
        else:
            try:
                validate_email(email)
            except:
                self.add_error("email","Please use another email address")

        if len(password) < 9:
            self.add_error("password","Password must have at least 8 characters")
        elif len(password) > 512:
            self.add_error("password","Password cannot be longer than 512 characters")

        try:
            usr = User.objects.get(username=username)
        except User.DoesNotExist:
            try:
                usr = User.objects.get(email=email)
            except User.DoesNotExist:
                cleaned_data["password"] = make_password(password)
            else:
                self.add_error("email","Email already exists")
        else:
            self.add_error("username","This username is already in use")