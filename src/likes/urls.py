from django.urls import path
from django.contrib.auth.decorators import login_required

from .views import PostLikeView

app_name = 'likes'
urlpatterns = [
    path(
      'posts/<int:id>/like/',
      login_required(PostLikeView.as_view()),
      name='post-likes'
    )
]
