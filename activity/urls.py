from django.urls import path
from .views import *

urlpatterns = [
    path("", Homepage.as_view(), name="homepage"),
    path("accounts", Accounts.as_view(), name="accounts"),
]
