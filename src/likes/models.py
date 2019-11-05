from django.db import models
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.conf import settings

from posts.models import Post


# Like Manager
class LikeManager(models.Manager):
  def find_is_liked(self, post, user):
    return self.filter(post=post, owner=user)

  def create_like(self, post, user):
    like = self.create(post=post, owner=user)
    like.save()


# LIKE MODEL
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

  objects = LikeManager()

  def __str__(self, *args, **kwargs):
    return self.post.title
