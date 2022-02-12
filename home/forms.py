from django import forms
from django.forms.widgets import PasswordInput, TextInput
from django.contrib.auth.hashers import make_password
from django.contrib.auth import get_user_model
from django.utils.translation import gettext as _
from home.models import UserDetail

from django.contrib.auth.models import User


class UserForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = ('username', 'password', 'email')
        error_messages = {
            'username': {
                'unique': _("Podany login jest już zajęty.")  # TRANSLATE TO ANNY LANGUAGE
            }
        }
        widgets = {
            'username': TextInput(attrs={'placeholder': 'Nazwa użytkownika'}),
            'password': PasswordInput(attrs={
                'class': 'form-control',
                'placeholder': 'Tajne hasło:'
            }),
            'email': TextInput(attrs={'placeholder': 'Adres e-mail'})
        }

    def save(self, commit=True, *args, **kwargs):
        m = super().save(commit=False)
        m.password = make_password(self.cleaned_data.get('password'))
        m.username = self.cleaned_data.get('username').lower()

        if commit:
            m.save()
        return m


class UserDetailForm(forms.ModelForm):
    class Meta:
        model = UserDetail
        fields = '__all__'
