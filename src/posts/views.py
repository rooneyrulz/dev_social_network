from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View, DetailView, UpdateView, DeleteView

from .models import Post
from .forms import PostForm


# POST LIST VIEW
class PostListView(View):
  model = Post
  form = PostForm
  template_name = 'posts/post_list.html'
  context = {}

  def get(self, request, *args, **kwargs):
    qs = self.model.objects.get_posts()
    form = self.form()
    self.context['title'] = 'Posts'
    self.context['posts'] = qs
    self.context['form'] = form
    return render(request, self.template_name, self.context)

  def post(self, request, *args, **kwargs):
    form = self.form(request.POST)
    if form.is_valid():
      instance = form.save(commit=False)
      instance.owner = self.request.user
      instance.save()
      messages.success(request, 'Post has been added to feed!')
      return redirect('posts:posts-list')
    messages.error(request, 'Oop! Enter valid details!')
    return reverse('posts:posts-list')


# POST DETAIL VIEW
class PostDetailView(DetailView):
  queryset = Post.objects.all()
  context_object_name = 'post'
  lookup = 'id'
  
  def get_object(self, *args, **kwargs):
    return get_object_or_404(Post, pk=self.kwargs.get(self.lookup))
  
  def get_context_data(self, *args, **kwargs):
    context = super(PostDetailView, self).get_context_data(*args, **kwargs)
    context['title'] = 'Post Detail'
    return context


# POST UPDATE VIEW
class PostUpdateView(LoginRequiredMixin, UpdateView):
  queryset = Post.objects.all()
  form_class = PostForm
  context_object_name = 'post'
  template_name = 'posts/post_update.html'
  lookup = 'id'

  def get_object(self, *args, **kwargs):
    return Post.objects.get_user_post(
      self.kwargs.get(self.lookup),
      self.request.user
    )

  def get_context_data(self, *args, **kwargs):
    context = super(PostUpdateView, self).get_context_data(*args, **kwargs)
    context['title'] = 'Post Update'
    return context
  
  def get_success_url(self, *args, **kwargs):
    messages.success(self.request, 'Post has been updated successfully!')
    return reverse('posts:posts-detail', kwargs={'id': self.kwargs.get(self.lookup)})


# POST DELETE VIEW
class PostDeleteView(LoginRequiredMixin, DeleteView):
  queryset = Post.objects.all()
  context_object_name = 'post'
  template_name = 'posts/post_delete.html'
  lookup = 'id'

  def get_object(self, *args, **kwargs):
    return Post.objects.get_user_post(
      self.kwargs.get(self.lookup),
      self.request.user
    )
  
  def get_context_data(self, *args, **kwargs):
    context = super(PostDeleteView, self).get_context_data(*args, **kwargs)
    context['title'] = 'Post Delete'
    return context

  def get_success_url(self, *args, **kwargs):
    messages.success(self.request, 'Post has been deleted!')
    return reverse('posts:posts-list')
