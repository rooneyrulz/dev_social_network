from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.models import User


class RegisterForm(forms.ModelForm):
  username = forms.CharField(
    widget=forms.TextInput(
      attrs={
        'class': 'form-control form-control-lg',
        'placeholder': 'Enter Username'
      }
    )
  )

  email = forms.EmailField(
    widget=forms.EmailInput(
      attrs={
        'class': 'form-control form-control-lg',
        'placeholder': 'Enter Email Id'
      }
    )
  )

  password = forms.CharField(
    widget=forms.PasswordInput(
      attrs={
        'class': 'form-control form-control-lg',
        'placeholder': 'Enter Password'
      }
    )
  )

  class Meta:
    model = User
    fields = ('username', 'email', 'password',)

  def clean_email(self, *args, **kwargs):
    email = self.cleaned_data.get('email')
    qs = User.objects.filter(email__contains=email)
    if qs.exists():
      raise forms.ValidationError('Email has already been registered!')
    else:
      return email


class LoginForm(forms.Form):
  username = forms.CharField(
    widget=forms.TextInput(
      attrs={
        'class': 'form-control form-control-lg',
        'placeholder': 'Enter username'
      }
    )
  )
  password = forms.CharField(
    widget=forms.PasswordInput(
      attrs={
        'class': 'form-control form-control-lg',
        'placeholder': 'Enter Password'
      }
    )
  )
