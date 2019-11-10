from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, UpdateView, DeleteView

from .models import Comment
from posts.models import Post
from .forms import CommentForm


# COMMENT CREATE VIEW
class CommentCreateView(LoginRequiredMixin, CreateView):
  queryset = Comment.objects.all()
  form_class = CommentForm
  template_name = 'comments/comment_create.html'

  def get_object(self, *args, **kwargs):
    return get_object_or_404(
      Post,
      pk=self.kwargs.get('id')
    )

  def form_valid(self, form):
    print(form.instance)
    if self.get_object():
      form.instance.post = self.get_object()
      form.instance.owner = self.request.user
      return super(CommentCreateView, self).form_valid(form)

  def get_context_data(self, *args, **kwargs):
    context = super(
      CommentCreateView, self
    ).get_context_data(*args, **kwargs)
    context['title'] = 'Comment Create'
    context['post'] = self.get_object()
    return context

  def get_success_url(self, *args, **kwargs):
    messages.success(self.request, 'Comment has been added!')
    return reverse('posts:posts-detail', kwargs={'id': self.get_object().pk})


# COMMENT DELETE VIEW
class CommentDeleteView(LoginRequiredMixin, DeleteView):
  queryset = Comment.objects.all()
  context_object_name = 'comment'
  template_name = 'comments/comment_delete.html'

  def get_object(self, *args, **kwargs):
    return Comment.objects.get_comment(
      self.kwargs.get('post_id'),
      self.kwargs.get('comment_id'),
      self.request.user
    )
  
  def get_context_data(self, *args, **kwargs):
    context = super(
      CommentDeleteView, self
    ).get_context_data(*args, **kwargs)
    context['title'] = 'Delete Comment'
    return context
  
  def get_success_url(self, *args, **kwargs):
    messages.success(
      self.request,
      'Comment has been deleted successfully!'
    )
    return reverse(
      'posts:posts-detail',
      kwargs={'id': self.get_object().post.pk}
    )


# COMMENT UPDATE VIEW
class CommentUpdateView(LoginRequiredMixin, UpdateView):
  queryset = Comment.objects.all()
  form_class = CommentForm
  template_name = 'comments/comment_update.html'

  def get_object(self, *args, **kwargs):
    return Comment.objects.get_comment(
      self.kwargs.get('post_id'),
      self.kwargs.get('comment_id'),
      self.request.user
    )
  
  def form_valid(self, form):
    print(form.instance)
    if self.get_object():
      return super(CommentUpdateView, self).form_valid(form)
  
  def get_context_data(self, *args, **kwargs):
    context = super(
      CommentUpdateView, self
    ).get_context_data(*args, **kwargs)
    context['title'] = 'Update Comment'
    context['comment'] = self.get_object()
    return context

  def get_success_url(self, *args, **kwargs):
    messages.success(
      self.request,
      'Comment has been updated successfully!'
    )
    return reverse(
      'posts:posts-detail',
      kwargs={'id': self.get_object().post.pk}
    )
