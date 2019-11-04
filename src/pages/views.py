from django.shortcuts import render
from django.views.generic import View


class IndexView(View):
  def get(self, request, *args, **kwargs):
    return render(request, 'pages/home.html', {})

class DashboardView(View):
  def get(self, request, *args, **kwargs):
    return render(request, 'pages/dashboard.html', {})

class AboutView(View):
  def get(self, request, *args, **kwargs):
    return render(request, 'pages/about.html', {})
