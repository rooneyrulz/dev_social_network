from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import IndexView, DashboardView, AboutView

app_name = 'pages'
urlpatterns = [
    path(
        'home/',
        IndexView.as_view(),
        name='home-view'
    ),
    path(
        'dashboard/',
        login_required(DashboardView.as_view()),
        name='dashboard-view'
    ),
    path(
        'about/',
        AboutView.as_view(),
        name='about-view'
    )
]
