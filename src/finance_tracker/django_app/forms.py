"""Labeled inputs for the explicitly selected USD synthetic opening."""

from django import forms

from .account_rules import clean_account_name, parse_opening_balance


class AccountCreationForm(forms.Form):
    name = forms.CharField(
        label="Hesap adı", max_length=100,
        help_text="Deneme hesabınız için benzersiz bir ad seçin (en fazla 100 karakter).",
        widget=forms.TextInput(attrs={"autofocus": True, "autocomplete": "off"}),
    )
    currency = forms.ChoiceField(
        label="Para birimi", choices=[("", "Para birimi seçin"), ("USD", "USD — ABD doları (2 ondalık basamak)")],
        help_text="Bu prototip için USD seçin. İlk finansal kayıttan sonra para birimi değiştirilemez.",
    )
    opening_balance = forms.CharField(
        label="Açılış bakiyesi (USD)", max_length=64,
        help_text="Deneme amaçlı başlangıç tutarıdır; yeni birikim sayılmaz. Ondalık ayırıcı olarak nokta kullanın (örnek: 1000.00). Sıfır veya pozitif tutar, en fazla 2 ondalık basamak; virgül kullanmayın.",
        widget=forms.TextInput(attrs={"inputmode": "decimal", "placeholder": "1000.00", "autocomplete": "off"}),
    )
    submission_key = forms.UUIDField(widget=forms.HiddenInput)

    def clean_name(self):
        try:
            return clean_account_name(self.cleaned_data["name"])
        except ValueError as error:
            raise forms.ValidationError(str(error)) from None

    def clean_opening_balance(self):
        value = self.cleaned_data["opening_balance"]
        try:
            parse_opening_balance(value)
        except ValueError as error:
            raise forms.ValidationError(str(error)) from None
        return value
