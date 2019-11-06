from django.urls import path
from django.contrib.auth.decorators import login_required

from .views import CreateCommentView

app_name = 'comments'
urlpatterns = [
    path(
      'posts/<int:id>/comments',
      login_required(CreateCommentView.as_view()),
      name='comments-create'
    )
]
