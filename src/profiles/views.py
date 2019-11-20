from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404
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
from .forms import ProfileForm, EducationForm


# PROFILE MIXINS
class ProfileObjectMixin(object):
  model = Profile
  lookup = 'id'

  def get_object(self, *args, **kwargs):
    return self.model.objects.get_auth_profile(
      self.kwargs.get(self.lookup),
      self.request.user
    )

class CheckAuthProfileMixin(object):
  model = Profile

  def get_object(self, *args, **kwargs):
    obj = self.model.objects.check_auth_profile(self.request.user)
    if not obj is None:
      return reverse('profiles:profiles-detail', kwargs={'id': obj.pk})
    else:
      return None


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
class ProfileCreateView(LoginRequiredMixin, CheckAuthProfileMixin, CreateView):
  queryset = Profile.objects.all()
  template_name = 'profiles/profile_create.html'
  form_class = ProfileForm

  def form_valid(self, form):
    form.instance.user = self.request.user
    messages.success(self.request, 'Profile has been created successfully!')
    return super(ProfileCreateView, self).form_valid(form)

  def get_context_data(self, *args, **kwargs):
    if self.get_object() is None:
      context = super(ProfileCreateView, self).get_context_data(*args, **kwargs)
      context['title'] = 'Create Profile'
      return context


# PROFILE DETAIL VIEW
class ProfileDetailView(LoginRequiredMixin, DetailView):
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
class ProfileUpdateView(
  LoginRequiredMixin,
  ProfileObjectMixin,
  UpdateView
):
  queryset = Profile.objects.all()
  context_object_name = 'profile'
  template_name = 'profiles/profile_update.html'
  form_class = ProfileForm

  def get_context_data(self, *args, **kwargs):
    if self.get_object():
      context = super(ProfileUpdateView, self).get_context_data(*args, **kwargs)
      context['title'] = 'Update Profile'
      return context
  
  def get_success_url(self, *args, **kwargs):
    messages.success(self.request, 'Profile has been updated successfully!')
    return reverse(
      'profiles:profiles-detail', kwargs={'id': self.get_object().pk}
    )


# PROFILE DELETE VIEW
class ProfileDeleteView(
  LoginRequiredMixin,
  ProfileObjectMixin,
  DeleteView
):
  queryset = Profile.objects.all()
  context_object_name = 'profile'
  template_name = 'profiles/profile_delete.html'

  def get_context_data(self, *args, **kwargs):
    if self.get_object():
      context = super(ProfileDeleteView, self).get_context_data(*args, **kwargs)
      context['title'] = 'Delete Profile'
      return context
  
  def get_success_url(self, *args, **kwargs):
    messages.success(self.request, 'Profile has been deleted successfully!')
    return reverse('profiles:profiles-list')


#######################EDUCATION VIEWS##################################


# EDUCATION MIXINS
class EducationProfileObjectMixin(object):
  model = Education
  profile_lookup = 'profile_id'
  education_lookup = 'education_id'

  def get_object(self, *args, **kwargs):
    return self.model.objects.get_profile_education(
      self.kwargs.get(self.profile_lookup),
      self.kwargs.get(self.education_lookup)
    )

class EducationObjectMixin(object):
  model = Profile
  lookup = 'id'

  def get_object(self, *args, **kwargs):
    return self.model.objects.get_auth_profile(
      self.kwargs.get(self.lookup),
      self.request.user
    )


# EDUCATION LIST VIEW
class EducationListView(
  LoginRequiredMixin,
  EducationObjectMixin,
  ListView
):
  queryset = Education.objects.all()
  context_object_name = 'educations'
  template_name = 'educations/education_list.html'

  def get_queryset(self, *args, **kwargs):
    return Education.objects.filter(profile=self.get_object().pk)

  def get_context_data(self, *args, **kwargs):
    context = super(EducationListView, self).get_context_data(*args, **kwargs)
    context['title'] = 'Educations'
    context['profile'] = self.get_object()
    return context


# EDUCATION DETAIL VIEW
class EducationDetailView(
  LoginRequiredMixin,
  EducationProfileObjectMixin,
  DetailView
):
  queryset = Education.objects.all()
  context_object_name = 'edu'
  template_name = 'educations/education_detail.html'

  def get_context_data(self, *args, **kwargs):
    context = super(EducationDetailView, self).get_context_data(*args, **kwargs)
    context['title'] = 'Education Detail'
    return context


# EDUCATION UPDATE VIEW
class EducationUpdateView(
  LoginRequiredMixin,
  EducationProfileObjectMixin,
  UpdateView
):
  queryset = Education.objects.all()
  context_object_name = 'edu'
  template_name = 'educations/education_update.html'
  form_class = EducationForm

  def get_context_data(self, *args, **kwargs):
    context = super(EducationUpdateView, self).get_context_data(*args, **kwargs)
    context['title'] = 'Education Update'
    return context

  def get_success_url(self, *args, **kwargs):
    messages.success(self.request, 'Education has been successfully updated!')
    return reverse(
      'profiles:educations-detail',
      kwargs={
        'profile_id': self.kwargs.get('profile_id'),
        'education_id': self.kwargs.get('education_id')
      }
    )


# EDUCATION DELETE VIEW
class EducationDeleteView(
  LoginRequiredMixin,
  EducationProfileObjectMixin,
  DeleteView
):
  queryset = Education.objects.all()
  context_object_name = 'edu'
  template_name = 'educations/education_delete.html'

  def get_context_data(self, *args, **kwargs):
    context = super(EducationDeleteView, self).get_context_data(*args, **kwargs)
    context['title'] = 'Education Delete'
    return context

  def get_success_url(self, *args, **kwargs):
    messages.success(self.request, 'Education has been successfully deleted!')
    return reverse(
      'profiles:educations-list',
      kwargs={
        'id': self.kwargs.get('profile_id'),
      }
    )


# EDUCATION CREATE VIEW
class EducationCreateView(
  LoginRequiredMixin,
  EducationObjectMixin,
  CreateView
):
  queryset = Education.objects.all()
  template_name = 'educations/education_create.html'
  form_class = EducationForm

  def form_valid(self, form):
    if self.get_object():
      form.instance.profile = self.get_object()
      messages.success(self.request, 'Education has been created successfully!')
      return super(EducationCreateView, self).form_valid(form)

  def get_context_data(self, *args, **kwargs):
    if self.get_object():
      context = super(EducationCreateView, self).get_context_data(*args, **kwargs)
      context['title'] = 'Education Create'
      return context
