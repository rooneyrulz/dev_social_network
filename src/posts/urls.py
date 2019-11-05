from django.urls import path

from .views import (
    PostListView,
    PostDetailView,
    PostUpdateView,
    PostDeleteView
)


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
    ),
    path(
        'posts/<int:id>/update/',
        PostUpdateView.as_view(),
        name='posts-update'
    ),
    path(
        'posts/<int:id>/delete/',
        PostDeleteView.as_view(),
        name='posts-delete'
    )
]
