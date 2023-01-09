from django.contrib import admin
from django.urls import path, include

from . import views
from .lettings.urls import letting_patterns
from .profiles.urls import profile_patterns

urlpatterns = [
    path('', views.welcome, name='welcome'),
    path("lettings/", include(letting_patterns)),
    path("profiles/", include(profile_patterns)),
    path('admin/', admin.site.urls)
]
