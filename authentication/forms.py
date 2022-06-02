from socket import fromshare
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from .models import AuthenticationPost
from .models import Post, FollowerRequest, AccBlogSettings


class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    email2 = forms.EmailField(label="Email confirmation", required=True, help_text='Enter the same password as before, for verification.')
    def clean_email2(self):
        email = self.cleaned_data.get('email')
        email2 = self.cleaned_data.get('email2')


        if email and email2 and email != email2:
            raise ValidationError("The two email fields didn’t match.")

        return email2

    class Meta:
        model = User
        fields = ["username", "email", "email2", "password1", "password2"]


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'description']

# class AuthenticationPostForm(forms.ModelForm):
#     class Meta:
#         model = AuthenticationPost
#         fields = ['title', 'description']

class FollowerRequestForm(forms.ModelForm):
    class Meta:
        model = FollowerRequest
        fields = ['account_id1']




#edycja profilu
class EditProfileForm(forms.ModelForm):
    is_private = forms.BooleanField(label="Tryb widoczności profilu",
                        help_text="Tylko obserwujący mogą przeglądac treść prywatnych kont",
                        required=False) #żeby mogło zostać niezaznaczone - blog nieprywatny
    bio = forms.CharField(label="Bio", max_length=250,
                          help_text="Opis bloga widoczny na profilu. Maksymalnie 250 znaków.")
    
        
    class Meta:
        model = AccBlogSettings
        fields = ["profile_background_colour", "window_colour", "border_colour",
                  "profile_picture", "bio", "is_private"]
