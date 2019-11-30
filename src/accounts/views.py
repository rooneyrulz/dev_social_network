from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import get_user_model
from django.views.generic import View, CreateView
from django.contrib import messages
from django.urls import reverse

from .forms import RegisterForm, LoginForm

User = get_user_model()


# REGISTRATION VIEW
class RegisterView(CreateView):
  model = User
  form_class = RegisterForm
  template_name = 'accounts/register.html'
  success_url = '/dev/accounts/login'

  def form_valid(self, form):
    messages.success(self.request, 'User has been registered successfully!')
    return super(RegisterView, self).form_valid(form)

  def get_context_data(self, **kwargs):
    context = super(RegisterView, self).get_context_data(**kwargs)
    context['title'] = 'Register'
    return context


# LOGIN VIEW
class LoginView(View):
  form = LoginForm
  template_name = 'accounts/login.html'
  context = {}

  def get(self, request, *args, **kwargs):
    form = self.form()
    self.context['title'] = 'Login'
    self.context['form'] = form
    return render(request, self.template_name, self.context)

  def post(self, request, *args, **kwargs):
    form = self.form(request.POST)
    if form.is_valid():
      user = form.cleaned_data.get('user_obj')
      login(request, user)
      messages.success(request, 'Yay! You just logged in!')
      return redirect(reverse('pages:dashboard-view'))
    self.context['title'] = 'Login'
    self.context['form'] = form
    return render(request, self.template_name, self.context)


class LogoutView(View):
  def get(self, request, *args, **kwargs):
    logout(request)
    messages.success(request, 'You has been logged out successfully!')
    return redirect(reverse('accounts:accounts-login'))
