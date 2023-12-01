from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class SignUp(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password',
            'password1'
        ]
        
class Login(AuthenticationForm):
    class Meta:
        model = User
        fields = [
            'username',
            'password'
        ]        