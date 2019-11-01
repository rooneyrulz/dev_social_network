from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('pages.urls', namespace='pages')),
    path('', include('posts.urls', namespace='posts')),
    path('admin/', admin.site.urls),
]
