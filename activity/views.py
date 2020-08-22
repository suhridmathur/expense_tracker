from decimal import Decimal

from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView

from .models import Account

@method_decorator(login_required, name="dispatch")
class Homepage(TemplateView):
    template_name = "homepage.html"

@method_decorator(login_required, name="dispatch")
class Accounts(TemplateView):
    template_name = "accounts.html"

    def get(self, request):
        data = self.get_context_data(request)
        return render(request, self.template_name, data)

    def get_context_data(self, request):
        accounts = Account.objects.filter(user=request.user)
        return {"accounts": accounts}

    def validate_and_prepare_account_data(self, request):
        account_data = {}
        if not request.POST.get("name"):
            return False, "Please enter account name", {}

        elif not request.POST.get("balance"):
            return False, "Please select initial balance", {}

        elif not request.FILES.get("logo"):
            return False, "Please upload a file", {}

        file_name = request.FILES.get("logo").name
        extension = file_name.split(".")[-1]

        if extension not in ("jpg", "jpeg", "png"):
            return False, "Invalid file format", {}

        account_data["balance"] = Decimal(request.POST.get("balance"))
        account_data["name"] = request.POST.get("name")
        account_data["logo"] = request.FILES.get("logo")
        account_data["user"] = request.user

        return True, "Account added successfully", account_data


    def post(self, request):
        status_code = 201
        success, message, account_data = self.validate_and_prepare_account_data(request)
        account = Account.objects.create(**account_data)
        if not success:
            status_code = 400
        return JsonResponse({"message": message}, status=status_code)


class Transactions(TemplateView):
    template_name = "transactions.html"