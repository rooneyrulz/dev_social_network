from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
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
      form.save()
      messages.success(request, 'Post has been added to feed!')
      return redirect('/posts')
    messages.error(request, 'Oop! Enter valid details!')
    return redirect('/posts')
    # return render(request, self.template_name, self.context)


# POST DETAIL VIEW
class PostDetailView(DetailView):
  queryset = Post.objects.all()
  context_object_name = 'post'
  
  def get_object(self, *args, **kwargs):
    return get_object_or_404(Post, pk=self.kwargs.get('id'))


# POST UPDATE VIEW
class PostUpdateView(UpdateView):
  pass


# POST DELETE VIEW
class PostDeleteView(DeleteView):
  pass

