from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm

from users.models import CustomUser


class CustomRegisterForm(UserCreationForm):
    street = forms.CharField(max_length=60, help_text="street")

    class Meta:
        model = CustomUser
        fields = ["username", "password1", "password2", "email", "street"]


class CustomUserEditForm(ModelForm):
    class Meta:
        model = CustomUser
        fields = [
            "phone_number",
            "street",
            "house_number",
            "apartment_number",
            "zip_code",
            "city",
            "country",
        ]
