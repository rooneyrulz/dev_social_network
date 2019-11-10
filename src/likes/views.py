from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View

from posts.models import Post
from .models import Like
from unlikes.models import Unlike


# POST LIKE VIEW
class PostLikeView(LoginRequiredMixin, View):
  lookup = 'id'

  def get_object(self, *args, **kwargs):
    return get_object_or_404(Post, pk=self.kwargs.get(self.lookup))

  def get(self, request, id=None, *args, **kwargs):
    is_liked = Like.objects.find_is_liked(
      self.get_object(),
      request.user
    )

    if is_liked.exists():
      messages.error(request, 'Post has already been liked!')
      return redirect(reverse('posts:posts-list'))
    else:
      is_unliked = Unlike.objects.find_is_unliked(
        self.get_object(),
        request.user
      )

      if is_unliked.exists():
        is_unliked.delete()
        Like.objects.create_like(self.get_object(), request.user)
        messages.success(request, 'Post has been liked!')
        return redirect(reverse('posts:posts-list'))
      else:
        Like.objects.create_like(self.get_object(), request.user)
        messages.success(request, 'Post has been liked!')
        return redirect(reverse('posts:posts-list'))




