from socket import fromshare
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Post

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    #email = forms.EmailField(required=True, label='podaj email swój testtest') #to dziala
    #email.label też działa

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
        #User.username.label = 'nazwa'
    
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'description']
