from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path(
        '',
        include('pages.urls', namespace='pages')
    ),
    path(
        '',
        include('accounts.urls', namespace='accounts')
    ),
    path(
        '',
        include('posts.urls', namespace='posts')
    ),
    path(
        '',
        include('likes.urls', namespace='likes')
    ),
    path(
        '',
        include('unlikes.urls', namespace='unlikes')
    ),
    path(
        '',
        include('comments.urls', namespace='comments')
    ),
    path('admin/', admin.site.urls),
]
