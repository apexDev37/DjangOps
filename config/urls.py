"""URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
"""

from django.contrib import admin
from django.urls import include, path

from config.settings.dev import ENABLE_DEBUG_TOOLBAR

urlpatterns = [
    path("admin/", admin.site.urls),
]

if ENABLE_DEBUG_TOOLBAR:
    urlpatterns.extend(
        [
            path("__debug__/", include("debug_toolbar.urls")),
        ]
    )
