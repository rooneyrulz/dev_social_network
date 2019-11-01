from django.shortcuts import render
from django.views.generic import ListView

from .models import Post


class PostListView(ListView):
  queryset = Post.objects.get_posts()
  context_object_name = 'posts'

  def get_context_data(self, **kwargs):
    context = super(PostListView, self).get_context_data(**kwargs)
    context['title'] = 'Posts'
    return context
