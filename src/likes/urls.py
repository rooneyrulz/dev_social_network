from django.urls import path
from .views import PostLikeView

app_name = 'likes'
urlpatterns = [
    path(
      'posts/<int:id>/like/',
      PostLikeView.as_view(),
      name='post-likes'
    )
]
