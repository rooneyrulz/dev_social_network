from django.urls import path
from .views import PostUnlikeView

app_name = 'unlikes'
urlpatterns = [
    path(
      'posts/<int:id>/unlike/',
      PostUnlikeView.as_view(),
      name='post-unlikes'
    )
]
