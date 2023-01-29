from django.contrib import admin
from django.urls import path, include

from . import views
from .lettings.urls import letting_patterns
from .profiles.urls import profile_patterns

def trigger_error(request):
    return 1/0

urlpatterns = [
    path('', views.welcome, name='welcome'),
    path('trigger/', trigger_error),
    path("lettings/", include(letting_patterns)),
    path("profiles/", include(profile_patterns)),
    path('admin/', admin.site.urls)
]
