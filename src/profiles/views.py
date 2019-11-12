from django.shortcuts import render
from django.views.generic import View, ListView


class ProfileListView(ListView):
  queryset = None
  template_name = 'profiles/profile_list.html'

  def get_queryset(self, *args, **kwargs):
    return None
