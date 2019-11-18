from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.urls import reverse
from django.views.generic import (
  View,
  ListView,
  CreateView,
  DetailView,
  UpdateView,
  DeleteView
)

from .models import Profile, Education, Experience, Social
from .forms import ProfileForm


# PROFILE LIST VIEW
class ProfileListView(ListView):
  queryset = Profile.objects.all()
  context_object_name = 'profiles'
  template_name = 'profiles/profile_list.html'

  def get_context_data(self, *args, **kwargs):
    context = super(ProfileListView, self).get_context_data(*args, **kwargs)
    context['title'] = 'Profiles'
    return context


# PROFILE CREATE VIEW
class ProfileCreateView(LoginRequiredMixin, CreateView):
  queryset = Profile.objects.all()
  template_name = 'profiles/profile_create.html'
  form_class = ProfileForm

  def get_object(self, *args, **kwargs):
    profile = Profile.objects.check_user_profile(self.request.user)
    if profile:
      return redirect(
        reverse('profiles:profiles-detail', kwargs={'id':profile.pk})
      )
    else:
      return None

  def form_valid(self, form):
    if self.get_object() is None:
      form.instance.user = self.request.user
      messages.success(self.request, 'Profile has been created successfully!')
      return super(ProfileCreateView, self).form_valid(form)

  
  def get_context_data(self, *args, **kwargs):
    context = super(ProfileCreateView, self).get_context_data(*args, **kwargs)
    context['title'] = 'Create Profile'
    return context


# PROFILE DETAIL VIEW
class ProfileDetailView(DetailView):
  queryset = Profile.objects.all()
  context_object_name = 'profile'

  def get_object(self, *args, **kwargs):
    return get_object_or_404(
      Profile,
      pk=self.kwargs.get('id')
    )

  def get_context_data(self, *args, **kwargs):
    context = super(ProfileDetailView, self).get_context_data(*args, **kwargs)
    context['title'] = self.get_object().name
    return context


# PROFILE UPDATE VIEW
class ProfileUpdateView(LoginRequiredMixin, UpdateView):
  queryset = Profile.objects.all()
  context_object_name = 'profile'
  template_name = 'profiles/profile_update.html'
  form_class = ProfileForm

  def get_object(self, *args, **kwargs):
    return Profile.objects.get_auth_profile(
      self.kwargs.get('id'),
      self.request.user
    )
  
  def get_context_data(self, *args, **kwargs):
    context = super(ProfileUpdateView, self).get_context_data(*args, **kwargs)
    context['title'] = 'Update Profile'
    return context
  
  def get_success_url(self, *args, **kwargs):
    messages.success(self.request, 'Profile has been updated successfully!')
    return reverse(
      'profiles:profiles-detail', kwargs={'id': self.get_object().pk}
    )


# PROFILE DELETE VIEW
class ProfileDeleteView(LoginRequiredMixin, DeleteView):
  queryset = Profile.objects.all()
  context_object_name = 'profile'
  template_name = 'profiles/profile_delete.html'

  def get_object(self, *args, **kwargs):
    return Profile.objects.get_auth_profile(
      self.kwargs.get('id'),
      self.request.user
    )

  def get_context_data(self, *args, **kwargs):
    context = super(ProfileDeleteView, self).get_context_data(*args, **kwargs)
    context['title'] = 'Delete Profile'
    return context
  
  def get_success_url(self, *args, **kwargs):
    messages.success(self.request, 'Profile has been deleted successfully!')
    return reverse('profiles:profiles-list')

