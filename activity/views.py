from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView

@method_decorator(login_required, name="dispatch")
class Homepage(TemplateView):
    template_name = "homepage.html"

@method_decorator(login_required, name="dispatch")
class Wallets(TemplateView):
    template_name = "wallets.html"