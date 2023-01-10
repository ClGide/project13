from django.urls import path

from . import views


profile_patterns = ([
    path('', views.profile_index, name='index'),
    path('<str:username>/', views.profile, name='profile')],
    "oc_lettings_site.profiles"
)
