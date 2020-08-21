from django.urls import path
from .views import *

urlpatterns = [
    path("", Homepage.as_view(), name="homepage"),
    path("wallets", Wallets.as_view(), name="wallets"),
]
