from django.urls import path

from . import views

letting_patterns = ([
    path('', views.index, name='index'),
    path('<int:letting_id>/', views.letting, name='letting')],
    "oc_lettings_site.lettings"
)
