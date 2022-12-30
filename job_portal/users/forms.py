from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class RegisterForm(UserCreationForm):
    email = (
        forms.EmailField(
            max_length=100,
            required=True,
            help_text="Please enter your email address",
            widget=forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Email address"}
            ),
        ),
    )
    # name = (
    #     forms.CharField(
    #         max_length=100,
    #         required=True,
    #         help_text="Please enter your name",
    #         widget=forms.TextInput(
    #             attrs={"class": "form-control", "placeholder": "Name"}
    #         ),
    #     ),
    # )
    first_name = (
        forms.CharField(
            max_length=100,
            required=True,
            help_text="Please enter your first name",
            widget=forms.TextInput(
                attrs={"class": "form-control", "placeholder": "First Name"}
            ),
        ),
    )
    last_name = (
        forms.CharField(
            max_length=100,
            required=True,
            help_text="Please enter your last name",
            widget=forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Last Name"}
            ),
        ),
    )
    username = (
        forms.CharField(
            max_length=100,
            required=True,
            help_text="Please enter your username",
            widget=forms.TextInput(
                attrs={"class": "form-control", "placeholder": "username"}
            ),
        ),
    )
    password1 = (
        forms.CharField(
            help_text="Please enter your password",
            required=True,
            widget=forms.TextInput(
                attrs={"class": "form-control", "placeholder": "password"}
            ),
        ),
    )
    password2 = (
        forms.CharField(
            help_text="Please enter your password again",
            required=True,
            widget=forms.TextInput(
                attrs={"class": "form-control", "placeholder": "password again"}
            ),
        ),
    )
    check = forms.BooleanField(required=True)

    class Meta:
        model = User
        fields = [
            "username",
            # "name",
            "email",
            "first_name",
            "last_name",
            "password1",
            "password2",
            "check",
        ]
