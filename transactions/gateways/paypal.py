# paypal.py

from .base import PaymentGateway
import paypalrestsdk
from django.conf import settings
from django.http import JsonResponse

paypalrestsdk.configure({
    "mode": settings.PAYPAL_MODE,
    "client_id": settings.PAYPAL_CLIENT_ID,
    "client_secret": settings.PAYPAL_CLIENT_SECRET
})


class PayPalGateway(PaymentGateway):
    def create_payment(self, transaction):
        payment = paypalrestsdk.Payment({
            "intent": "sale",
            "payer": {
                "payment_method": "paypal"
            },
            "redirect_urls": {
                "return_url": f"{settings.APP_API_URL}/execute-payment/",
                "cancel_url": f"{settings.APP_API_URL}/cancel-payment/",
            },
            "transactions": [{
                "amount": {
                    "total": str(transaction.amount),
                    "currency": transaction.currency
                },
                "description": transaction.description
            }]
        })

        if payment.create():
            return payment
        return None

    def execute_payment(self, transaction, **kwargs):
        payer_id = kwargs.get('payer_id')
        payment_id = kwargs.get('payment_id')

        payment = paypalrestsdk.Payment.find(payment_id)
        if payment.execute({"payer_id": payer_id}):
            transaction.status = 'Completed'
            transaction.save()
            return payment
        return None

    def cancel_payment(self, transaction):
        transaction.status = 'Cancelled'
        transaction.save()
        return JsonResponse({'message': 'Payment has been cancelled'}, status=200)
