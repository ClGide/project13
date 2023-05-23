from django.contrib import admin
from django.urls import path, include
from sentry_sdk import capture_exception

from . import views
from .lettings.urls import letting_patterns
from .profiles.urls import profile_patterns


def trigger_error():
    return 1 / 0

try:
    trigger_error()
except Exception as e:
    capture_exception(e)


urlpatterns = [
    path('', views.welcome, name='welcome'),
    path('sentry_debug/', trigger_error),
    path("lettings/", include(letting_patterns)),
    path("profiles/", include(profile_patterns)),
    path('admin/', admin.site.urls)
]
