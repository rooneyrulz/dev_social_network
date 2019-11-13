from django.urls import path
from .views import ProfileListView

app_name = 'profiles'
urlpatterns = [
    path('', ProfileListView.as_view(), name='profiles-list')
]

