from django.urls import path
from .views import RegisterView


app_name = 'accounts'
urlpatterns = [
    path('register', RegisterView.as_view(), name='accounts-register')
]
