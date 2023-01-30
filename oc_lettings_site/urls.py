from django.contrib import admin
from django.urls import path, include
from sentry_sdk import capture_message

from . import views
from .lettings.urls import letting_patterns
from .profiles.urls import profile_patterns


capture_message("Hello World")  # Will create an event in Sentry.

def trigger_error():
    return 1 / 0

urlpatterns = [
    path('', views.welcome, name='welcome'),
    path('sentry_debug/', trigger_error),
    path("lettings/", include(letting_patterns)),
    path("profiles/", include(profile_patterns)),
    path('admin/', admin.site.urls)
]
