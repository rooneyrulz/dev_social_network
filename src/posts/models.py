from django.db import models
from django.shortcuts import get_object_or_404
from django.conf import settings


class PostManager(models.Manager):
  def get_posts(self, *args, **kwargs):
    return self.all()

  def get_post(self, post_id, *args, **kwargs):
    return get_object_or_404(self, id=post_id)

  def get_user_posts(self, owner, *args, **kwargs):
    return self.filter(owner=owner)


class Post(models.Model):
  title = models.CharField(max_length=100)
  description = models.TextField()
  created_at = models.DateTimeField(auto_now_add=True)
  owner = models.ForeignKey(
    settings.AUTH_USER_MODEL,
    default=1,
    on_delete=models.CASCADE,
    null=True
  )

  objects = PostManager()

  def __str__(self, *args, **kwargs):
    return self.title


class Like(models.Model):
  post = models.ForeignKey(
    Post,
    default=1,
    on_delete=models.CASCADE
  )
  owner = models.ForeignKey(
    settings.AUTH_USER_MODEL,
    default=1,
    on_delete=models.CASCADE
  )

  def __str__(self, *args, **kwargs):
    return self.post


class Unlike(models.Model):
  post = models.ForeignKey(
    Post,
    default=1,
    on_delete=models.CASCADE
  )
  owner = models.ForeignKey(
    settings.AUTH_USER_MODEL,
    default=1,
    on_delete=models.CASCADE
  )

  def __str__(self, *args, **kwargs):
    return self.post


class Comment(models.Model):
  text = models.TextField(default="awesome!")
  post = models.ForeignKey(
    Post,
    default=1,
    on_delete=models.CASCADE
  )
  owner = models.ForeignKey(
    settings.AUTH_USER_MODEL,
    default=1,
    on_delete=models.CASCADE
  )

  def __str__(self, *args, **kwargs):
    return self.post