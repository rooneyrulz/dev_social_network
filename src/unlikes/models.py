from django.db import models
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.conf import settings

from posts.models import Post


# UNLIKE MANAGER
class UnlikeManager(models.Manager):
  def find_is_unliked(self, post, user):
    return self.filter(post=post, owner=user)


# UNLIKE MODEL
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

  objects = UnlikeManager()

  def __str__(self, *args, **kwargs):
    return self.post.title


