from PIL import Image ##nowe
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.core.files.uploadedfile import SimpleUploadedFile
from django.utils.safestring import mark_safe ##nowe
from .models import AuthenticationPost
from .models import Post, FollowerRequest, AccBlogSettings





class RegisterForm(UserCreationForm):
    username = forms.CharField(label="Nazwa użytkownika", required=True,
                               help_text="Pole wymagane. Do 150 znaków. Tylko litery, cyfry, i znaki @.+-_")
    email = forms.EmailField(label="E-mail", required=True)
    email2 = forms.EmailField(label="Potwierdź E-mail", required=True,
                              help_text='Powtórz ten sam adres E-mail co wcześniej, dla weryfikacji.')
    pass1HelpText = """<ul>
        <li>Hasło nie może być zbyt podobne do pozostałych informacji osobowych.</li>
        <li>Hasło musi mieć conajmniej 8 znaków.</li>
        <li>Hasło nie może znajdować się na liście najpopularniejszych haseł.</li>
        <li>Hasło nie może składać się z samych cyfr.</li>
    </ul>"""
    password1 = forms.CharField(label="Hasło", required=True, widget=forms.PasswordInput,
                                help_text=mark_safe(pass1HelpText))
    #       Your password can’t be too similar to your other personal information.
    #       Your password must contain at least 8 characters.
    #       Your password can’t be a commonly used password.
    #       Your password can’t be entirely numeric.
    password2 = forms.CharField(label="Potwierdź hasło", required=True, widget=forms.PasswordInput,
                                help_text="Powtórz to samo hasło co wcześniej, dla weryfikacji.")
    tos_accepted = forms.BooleanField(label=mark_safe('Akceptuję <a href="/tos">regulamin serwisu</a>'),
                        required=True) #nie da się zarejestrować bez akceptacji
    
    def clean_email2(self):
        email = self.cleaned_data.get('email')
        email2 = self.cleaned_data.get('email2')


        if email and email2 and email != email2:
            raise ValidationError("Podane adresy E-mail różnią się od siebie.")

        return email2

    class Meta:
        model = User
        fields = ["username", "email", "email2", "password1", "password2", "tos_accepted"]
#na ten moment jeszcze 4 ValidationErrory do haseł są dalej po angielsku!




class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'description']

# class AuthenticationPostForm(forms.ModelForm):
#     class Meta:
#         model = AuthenticationPost
#         fields = ['title', 'description']

class FollowerRequestForm(forms.Form):
    typ = (
        ("received", "Otrzymane Zaproszenia"),
        ("followed", "Obserwowani"),
        ("sended", "Wysłane zaproszenia")
    )
    zaproszenia = forms.ChoiceField(label='', choices=typ, required=False,
                        widget=forms.Select(attrs={'onchange': 'form.submit();'}))

# Wybór postów
wybor_postow = (
    ("Wszystkie", "Wszystkie"),
    ("Obserwowani", "Od obserwowanych"),
    #("Najlepsze", "Najlepsze")
)
okres_czasu = (
    ("day", "Z ostatniego dnia"),
    ("week", "Z ostatniego tygodnia"),
    ("month", "Z ostatniego miesiąca"),
    ("year", "Z ostatniego roku"),
    ("alltime", "Od początku")
)
class PostChooseForm(forms.Form):
    Typ = forms.ChoiceField(label='', choices=wybor_postow, required=False, #label jest osobno w htmlu jako <label> żeby był w linii z formularzem a nie w kolumnie z tym jednym polem
                            widget=forms.Select(attrs={'onchange': 'form.submit();'}))
    Czas = forms.ChoiceField(label='', choices=okres_czasu, required=False,
                             widget=forms.Select(attrs={'onchange': 'form.submit();'})) #.hidden_widget




#edycja profilu
class EditProfileForm(forms.ModelForm):
    username = forms.CharField(label="Zmień nazwę użytkownika", required=False)
    is_private = forms.BooleanField(label="Profil prywatny",
                        help_text="Tylko obserwujący mogą przeglądac treść prywatnych kont",
                        required=False) #żeby mogło zostać niezaznaczone - blog nieprywatny
    bio = forms.CharField(label="Bio", max_length=250, required=False,
                          help_text="Opis bloga widoczny na profilu. Maksymalnie 250 znaków.")
    profile_picture = forms.ImageField(label="Zdjęcie profilowe", required=False)
    KATEGORIE_TEMP = (("1", "Kateg. 1"), ("2", "Kateg. 2"),("3", "Kateg. 3"))
    category_offer = forms.ChoiceField(choices = KATEGORIE_TEMP, required=False)
    category_interested = forms.ChoiceField(choices = KATEGORIE_TEMP, required=False)
        
    class Meta:
        model = AccBlogSettings
        fields = ["username", "profile_background_colour", "window_colour", "border_colour",
                  "profile_picture", "bio", "is_private",
                  "category_offer", "category_interested"] #TEMPORARY! robie na 10 minut przed spotkaniem xD potem poprawie
