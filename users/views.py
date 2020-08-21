from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.generic.base import TemplateView

class Login(TemplateView):
    template_name = "login.html"

    def post(self, request, *args, **kwargs):
        email = request.POST.get("email", None)
        password = request.POST.get("password", None)
        
        if not (email and password):
            message = "Please provide email and password"
            return render(request, self.template_name, {"message": message})

        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            message = f"User with email {email} does not exist"
            return render(request, self.template_name, {"message": message})

        user = authenticate(request, username=user.username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect("/")
        else:
            message = f"Bad Credentials!"
            return render(request, self.template_name, {"message": message})
        return HttpResponseRedirect("/login/")


@method_decorator(login_required, name="dispatch")
class Logout(TemplateView):
    def get(self, request, *args, **kwargs):
        logout(request)
        return HttpResponseRedirect("/")