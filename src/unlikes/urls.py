from django.urls import path
from .views import PostUnlikeView

app_name = 'unlikes'
urlpatterns = [
    path(
      '<int:id>/unlike/',
      PostUnlikeView.as_view(),
      name='post-unlikes'
    )
]
