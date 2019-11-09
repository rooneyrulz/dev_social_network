from django.urls import path
from django.contrib.auth.decorators import login_required

from .views import CommentCreateView, CommentDeleteView, CommentUpdateView

app_name = 'comments'
urlpatterns = [
    path(
      'posts/<int:id>/comments/',
      login_required(CommentCreateView.as_view()),
      name='comments-create'
    ),
    path(
      'posts/<int:post_id>/comments/<int:comment_id>/',
      login_required(CommentDeleteView.as_view()),
      name='comments-delete'
    ),
    path(
      'posts/<int:post_id>/comments/<int:comment_id>/update/',
      login_required(CommentUpdateView.as_view()),
      name='comments-update'
    )
]
