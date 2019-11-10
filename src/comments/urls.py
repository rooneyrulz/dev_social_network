from django.urls import path
from .views import CommentCreateView, CommentDeleteView, CommentUpdateView

app_name = 'comments'
urlpatterns = [
    path(
      'posts/<int:id>/comments/',
      CommentCreateView.as_view(),
      name='comments-create'
    ),
    path(
      'posts/<int:post_id>/comments/<int:comment_id>/',
      CommentDeleteView.as_view(),
      name='comments-delete'
    ),
    path(
      'posts/<int:post_id>/comments/<int:comment_id>/update/',
      CommentUpdateView.as_view(),
      name='comments-update'
    )
]
