from django.urls import path
from django.contrib.auth.decorators import login_required

from .views import PostUnlikeView

app_name = 'unlikes'
urlpatterns = [
    path(
      'posts/<int:id>/unlike/',
      login_required(PostUnlikeView.as_view()),
      name='post-unlikes'
    )
]
