

from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class Subscription(models.Model):
    PLAN_CHOICES = [
        ('standard', 'Standard'),
        ('family_restricted', 'Famille restreint'),
        ('family_extended', 'Famille élargie'),
    ]

    PLAN_PRICES = {
        'standard': 5.00,
        'family_restricted': 10.00,
        'family_extended': 15.00,
    }

    account_number = models.CharField(max_length=100)
    plan = models.CharField(max_length=20, choices=PLAN_CHOICES)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.account_number} - {self.plan}"


class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.email} - {self.created_at}"


class Transaction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subscription = models.ForeignKey(Subscription, on_delete=models.CASCADE)
    transaction_id = models.CharField(max_length=100, unique=True)
    payment_token = models.CharField(max_length=255)
    payment_url = models.URLField(max_length=500)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.transaction_id} - {self.user.username}"
