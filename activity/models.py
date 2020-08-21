from django.contrib.auth.models import User
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Account(models.Model):
    name = models.CharField(max_length=100)
    balance = models.DecimalField(max_digits=10, decimal_places=2)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Transaction(models.Model):
    class TransactionTypeChoices(models.TextChoices):
        EXPENSE = "expense", "Expense"
        INCOME = "income", "Income"
        INVESTEMENT = "investment", "Investment"
        ACCOUNT_TRANSFER = "account_transfer", "Account Transfer"

    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    account = models.ForeignKey(Account, on_delete=models.PROTECT)
    transaction_type = models.CharField(
        max_length=50, choices=TransactionTypeChoices.choices
    )

    def save(self, *args, **kwargs):
        self.account.balance -= self.amount
        self.account.save()
        super(Transaction, self).save(*args, **kwargs)


class InvestmentType(models.Model):
    name = models.CharField(max_length=500)


class Investment(models.Model):
    investment_amount = models.DecimalField(max_digits=10, decimal_places=2)
    return_amount = models.DecimalField(max_digits=10, decimal_places=2)
    invested_type = models.ForeignKey(InvestmentType, on_delete=models.PROTECT)
    timestamp = models.DateTimeField(auto_now_add=True)
    return_date = models.DateField(null=True, blank=True)
    description = models.TextField()
