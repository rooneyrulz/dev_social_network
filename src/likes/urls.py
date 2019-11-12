from django.urls import path
from .views import PostLikeView

app_name = 'likes'
urlpatterns = [
    path(
      '<int:id>/like/',
      PostLikeView.as_view(),
      name='post-likes'
    )
]
