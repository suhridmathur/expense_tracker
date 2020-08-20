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
        self.wallet.balance -= self.amount
        self.wallet.save()
        super(Transaction, self).save(*args, **kwargs)