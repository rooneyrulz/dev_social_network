from django.urls import path

from .views import IndexView

app_name = 'pages'
urlpatterns = [
    path(
        'home',
        IndexView.as_view(),
        name='home-view'
    )
]
