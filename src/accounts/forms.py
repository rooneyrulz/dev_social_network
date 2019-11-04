from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.models import User


class RegisterForm(forms.ModelForm):
  username = forms.CharField(
    widget=forms.TextInput(
      attrs={
        'placeholder': 'Enter Username'
      }
    )
  )

  email = forms.EmailField(
    widget=forms.EmailInput(
      attrs={
        'placeholder': 'Enter Email Id'
      }
    )
  )

  password = forms.CharField(
    widget=forms.PasswordInput(
      attrs={
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
        'placeholder': 'Enter username'
      }
    )
  )
  password = forms.CharField(
    widget=forms.PasswordInput(
      attrs={
        'placeholder': 'Enter Password'
      }
    )
  )

  def clean(self, *args, **kwargs):
    username = self.cleaned_data.get('username')
    password = self.cleaned_data.get('password')

    if username and password:
      user = authenticate(username=username, password=password)
      if not user:
        raise forms.ValidationError('User does not exist!')
      if not user.check_password(password):
        raise forms.ValidationError('Invalid password!')
      if not user.is_active:
        raise forms.ValidationError('User is not active!')
    return super(LoginForm, self).clean(*args, **kwargs)
