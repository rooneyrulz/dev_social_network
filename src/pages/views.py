from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View


class IndexView(View):
  def get(self, request, *args, **kwargs):
    return HttpResponse("Hello Devs")
