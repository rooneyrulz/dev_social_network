from django.urls import path

from .views import PostListView, PostDetailView


app_name = 'posts'
urlpatterns = [
    path(
        'posts/',
        PostListView.as_view(),
        name='posts-list'
    ),
    path(
        'posts/<int:id>/detail/',
        PostDetailView.as_view(),
        name='posts-detail'
    )
]
