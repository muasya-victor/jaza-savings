# payments/utils.py
from transactions.gateways.paypal import PayPalGateway
from transactions.gateways.kcb import KCBGateway


class PaymentGatewayFactory:
    @staticmethod
    def get_gateway(payment_gateway_name):
        if payment_gateway_name == 'paypal':
            return PayPalGateway()
        elif payment_gateway_name == 'kcb':
            return KCBGateway()
        else:
            raise ValueError("Unsupported payment gateway")
