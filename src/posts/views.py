from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.generic import View

from .models import Post
from .forms import PostForm


class PostListView(View):
  model = Post
  form = PostForm
  template_name = 'posts/post_list.html'
  context = {}

  def get(self, request, *args, **kwargs):
    qs = self.model.objects.get_posts()
    form = self.form()
    self.context = {
      'title': 'Posts',
      'posts': qs,
      'form': form
    }
    return render(request, self.template_name, self.context)

  def post(self, request, *args, **kwargs):
    form = self.form(request.POST)
    if form.is_valid():
      form.save()
      messages.success(request, 'Post has been added to feed!')
      return redirect('/posts')
    messages.error(request, 'Oop! Enter valid details!')
    return redirect('/posts')
