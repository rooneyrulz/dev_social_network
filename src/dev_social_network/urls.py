from django.contrib import admin
from django.conf import settings
from django.urls import path, include

urlpatterns = [
    path(
        'dev/',
        include('pages.urls', namespace='pages')
    ),
    path(
        'dev/accounts/',
        include('accounts.urls', namespace='accounts')
    ),
    path(
        'dev/posts/',
        include('posts.urls', namespace='posts')
    ),
    path(
        'dev/posts/',
        include('likes.urls', namespace='likes')
    ),
    path(
        'dev/posts/',
        include('unlikes.urls', namespace='unlikes')
    ),
    path(
        'dev/posts/',
        include('comments.urls', namespace='comments')
    ),
    path(
        'dev/profiles/',
        include('profiles.urls', namespace='profiles')
    ),
    path('admin/', admin.site.urls),
]


if settings.DEBUG:
    from django.conf.urls.static import static

    urlpatterns += static(
        settings.STATIC_URL,
        document_root=settings.STATIC_ROOT
    )
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )
