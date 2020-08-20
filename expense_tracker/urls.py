from django.contrib import admin
from django.urls import path, include

from activity import urls

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(urls)),
]
