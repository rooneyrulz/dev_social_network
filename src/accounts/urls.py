from django.urls import path
from .views import RegisterView, LoginView, LogoutView


app_name = 'accounts'
urlpatterns = [
    path(
        'register/',
        RegisterView.as_view(),
        name='accounts-register'
    ),
    path(
        'login/',
        LoginView.as_view(),
        name='accounts-login'
    ),
    path(
        'logout/',
        LogoutView.as_view(),
        name='accounts-logout'
    ),
]
