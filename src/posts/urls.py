from django.urls import path

from .views import PostListView


app_name = 'posts'
urlpatterns = [
    path(
        'posts',
        PostListView.as_view(),
        name='posts-list'
    )
]
