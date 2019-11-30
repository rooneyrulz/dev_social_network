from django import forms
from django.db.models import Q
from django.contrib.auth import get_user_model

User = get_user_model()


class RegisterForm(forms.ModelForm):
  email = forms.EmailField(
    widget=forms.EmailInput(
      attrs={
        'class': 'form-control form-control-lg',
        'placeholder': 'Enter Email Id'
      }
    )
  )

  password1 = forms.CharField(
    label='Password',
    widget=forms.PasswordInput(
      attrs={
        'class': 'form-control form-control-lg',
        'placeholder': 'Enter Password'
      }
    )
  )

  password2 = forms.CharField(
    label='Confirm Password',
    widget=forms.PasswordInput(
      attrs={
        'class': 'form-control form-control-lg',
        'placeholder': 'Confirm Password'
      }
    )
  )

  class Meta:
    model = User
    fields = ('email',)

  def clean_email(self, *args, **kwargs):
    email = self.cleaned_data.get('email')
    qs = User.objects.filter(email__contains=email)
    if qs.exists():
      raise forms.ValidationError('Email has already been registered!')
    else:
      return email

  def clean_password2(self, *args, **kwargs):
    password1 = self.cleaned_data.get('password1')
    password2 = self.cleaned_data.get('password2')
    if password1 and password2 and password1 != password2:
      raise forms.ValidationError('Passwords did not match!')
    else:
      return password2

  def save(self, commit=True):
    user = super(RegisterForm, self).save(commit=False)
    user.set_password(self.cleaned_data['password1'])
    if commit:
      user.save()
    return user


class LoginForm(forms.Form):
  email = forms.CharField(
    widget=forms.TextInput(
      attrs={
        'class': 'form-control form-control-lg',
        'placeholder': 'Enter Email'
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

  def clean(self, *args, **kwargs):
    email = self.cleaned_data.get('email')
    password = self.cleaned_data.get('password')
    qs = User.objects.filter(email__iexact=email)
    if not qs.exists():
      raise forms.ValidationError('User does not exist!')
    user_obj = qs.first()
    if not user_obj.check_password(password):
      raise forms.ValidationError('Invalid Credentials!')
    self.cleaned_data['user_obj'] = user_obj
    return super(LoginForm, self).clean(*args, **kwargs)

