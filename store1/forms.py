from django import forms
from store1 import models
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class CreatePostFrom(forms.ModelForm):
    class Meta:
        model = models.Post
        fields = ['title', 'description']

class RegisterForm(UserCreationForm):
    email = forms.EmailField()
   
    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'username', 'password1', 'password2' ]