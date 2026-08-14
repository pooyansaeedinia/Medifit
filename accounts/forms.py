from django import forms
from django.contrib.auth.forms import SetPasswordMixin, UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    # name = forms.CharField(
    #     max_length=150,
    #     required=True,
    #     widget=forms.TextInput(
    #         attrs={
    #             'class': 'form-control',
    #             'id': 'signup-name',
    #             'placeholder': 'Enter your full name',
    #         }
    #     )
    # )

    # email = forms.EmailField(
    #     required=True,
    #     widget=forms.EmailInput(
    #         attrs={
    #             'class': 'form-control',
    #             'id': 'signup-email',
    #             'placeholder': 'Enter your email',
    #         }
    #     )
    # )

    # password1 = forms.CharField(
    #     label='Password',
    #     widget=forms.PasswordInput(
    #         attrs={
    #             'class': 'form-control',
    #             'id': 'signup-password',
    #             'placeholder': 'Create a password',
    #         }
    #     )
    # )

    # password2 = forms.CharField(
    #     label='Confirm Password',
    #     widget=forms.PasswordInput(
    #         attrs={
    #             'class': 'form-control',
    #             'id': 'signup-confirmPassword',
    #             'placeholder': 'Confirm your password',
    #         }
    #     )
    # )

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    # def clean_email(self):
    #     email = self.cleaned_data['email']

    #     if User.objects.filter(email=email).exists():
    #         raise forms.ValidationError(
    #             'An account with this email already exists.'
    #         )

    #     return email

    # def save(self, commit=True):
    #     user = super().save(commit=False)

    #     user.username = self.cleaned_data['email']
    #     user.first_name = self.cleaned_data['name']

    #     if commit:
    #         user.save()

    #     return user


class PasswordResetSetForm(SetPasswordMixin, forms.Form):
    password1, password2 = SetPasswordMixin.create_password_fields(
        label1='New password',
        label2='New password confirmation',
    )

    def __init__(self, user, *args, **kwargs):
        self.user = user
        super().__init__(*args, **kwargs)

    def clean(self):
        self.validate_passwords('password1', 'password2')
        self.validate_password_for_user(self.user, 'password2')
        return super().clean()

    def save(self, commit=True):
        return self.set_password_and_save(self.user, 'password1', commit=commit)
