from django.contrib.auth.models import User
from django.db import models


class Subscription(models.Model):
    PLAN_CHOICES = [
        ('standard', 'Standard'),
        ('family_restricted', 'Famille restreint'),
        ('family_extended', 'Famille élargie'),
    ]

    account_number = models.CharField(max_length=100)
    plan = models.CharField(max_length=20, choices=PLAN_CHOICES)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.account_number} - {self.plan}"


class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.email} - {self.created_at}"
