from django.db import models
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from django.urls import reverse

from posts.models import Post

User = get_user_model()


# COMMENT MANAGER
class CommentManager(models.Manager):
  def get_comment(self, p_id, c_id, user):
    return get_object_or_404(self, post=p_id, pk=c_id, owner=user)


# COMMENT MODEL
class Comment(models.Model):
  text = models.TextField(default="awesome!")
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

  objects = CommentManager()

  def __str__(self, *args, **kwargs):
    return self.text

  def get_delete_url(self, *args, **kwargs):
    return reverse(
      'comments:comments-delete',
      kwargs={'post_id': self.post.pk, 'comment_id': self.pk}
    )

  def get_update_url(self, *args, **kwargs):
    return reverse(
      'comments:comments-update',
      kwargs={'post_id': self.post.pk, 'comment_id': self.pk}
    )
  