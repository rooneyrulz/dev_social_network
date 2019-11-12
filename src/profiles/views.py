from django.shortcuts import render
from django.views.generic import View, ListView

from .models import Profile


class ProfileListView(ListView):
  queryset = Profile.objects.all()
  context_object_name = 'profiles'
  template_name = 'profiles/profile_list.html'

  def get_context_data(self, *args, **kwargs):
    context = super(ProfileListView, self).get_context_data(*args, **kwargs)
    context['title'] = 'Profiles'
    return context

