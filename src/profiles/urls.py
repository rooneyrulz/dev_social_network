from django.urls import path
from .views import (
    ProfileListView,
    ProfileCreateView,
    ProfileDetailView,
    ProfileUpdateView,
    ProfileDeleteView,
    EducationListView,
    EducationCreateView,
    EducationDetailView,
    EducationUpdateView,
    EducationDeleteView
)

app_name = 'profiles'
urlpatterns = [
    path(
        '',
        ProfileListView.as_view(),
        name='profiles-list'
    ),
    path(
        'create/',
        ProfileCreateView.as_view(),
        name='profiles-create'
    ),
    path(
        '<int:id>/detail/',
        ProfileDetailView.as_view(),
        name='profiles-detail'
    ),
    path(
        '<int:id>/delete/',
        ProfileDeleteView.as_view(),
        name='profiles-delete'
    ),
    path(
        '<int:id>/update/',
        ProfileUpdateView.as_view(),
        name='profiles-update'
    ),
    path(
        '<int:id>/educations/',
        EducationListView.as_view(),
        name='educations-list'
    ),
    path(
        '<int:id>/educations/create',
        EducationCreateView.as_view(),
        name='educations-create'
    ),
    path(
        '<int:profile_id>/educations/<int:education_id>/detail',
        EducationDetailView.as_view(),
        name='educations-detail'
    ),
    path(
        '<int:profile_id>/educations/<int:education_id>/update',
        EducationUpdateView.as_view(),
        name='educations-update'
    ),
    path(
        '<int:profile_id>/educations/<int:education_id>/delete',
        EducationDeleteView.as_view(),
        name='educations-delete'
    ),
]

