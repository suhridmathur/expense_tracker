from django.contrib import admin
from django.urls import path, include

from activity import urls
from users import urls as user_urls

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(user_urls)),
    path("", include(urls)),
]
