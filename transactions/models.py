from django.db import models
from django.contrib.auth.models import User


class Transaction(models.Model):
    PAYMENT_GATEWAYS = [
        ('paypal', 'PayPal'),
        ('kcb', 'KCB'),
        ('mpesa', 'Mpesa'),
        ('equity', 'Equity'),
        ('national_bank', 'National Bank'),
        # Add more as needed
    ]

    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Completed', 'Completed'),
        ('Failed', 'Failed'),
        ('Canceled', 'Canceled'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.CharField(max_length=10, default='USD')
    payment_gateway = models.CharField(max_length=20, choices=PAYMENT_GATEWAYS)
    gateway_transaction_id = models.CharField(max_length=100, null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username} - {self.amount} {self.currency} - {self.status} - {self.payment_gateway}"
