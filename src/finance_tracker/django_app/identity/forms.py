"""Presentation and email normalization around Django's authentication form."""

from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm


class PrototypeAuthenticationForm(AuthenticationForm):
    username = forms.EmailField(
        label="E-posta",
        widget=forms.EmailInput(attrs={"autofocus": True, "autocomplete": "username"}),
    )
    password = forms.CharField(
        label="Şifre", strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "current-password"}),
    )
    error_messages = {
        "invalid_login": "E-posta adresi veya şifre hatalı.",
        "inactive": "Bu kullanıcı hesabı etkin değil.",
    }

    def clean_username(self):
        return get_user_model().objects.normalize_email(self.cleaned_data["username"])
