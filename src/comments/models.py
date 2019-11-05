from django.db import models
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.conf import settings

from posts.models import Post


# COMMENT MODEL
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
    return self.text