from django.db import models
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from django.urls import reverse

from posts.models import Post

User = get_user_model()


# UNLIKE MANAGER
class UnlikeManager(models.Manager):
  def find_is_unliked(self, post, user):
    return self.filter(post=post, owner=user)
  
  def create_unlike(self, post, user):
    unlike = self.create(post=post, owner=user)
    unlike.save()


# UNLIKE MODEL
class Unlike(models.Model):
  post = models.ForeignKey(
    Post,
    default=1,
    on_delete=models.CASCADE
  )
  owner = models.ForeignKey(
    User,
    default=1,
    on_delete=models.CASCADE
  )

  objects = UnlikeManager()

  def __str__(self, *args, **kwargs):
    return self.post.title


