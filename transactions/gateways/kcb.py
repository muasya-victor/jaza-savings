from .base import PaymentGateway


class KCBGateway(PaymentGateway):
    def create_payment(self, transaction):
        # KCB specific logic
        pass

    def execute_payment(self, transaction, **kwargs):
        # KCB specific logic
        pass

    def cancel_payment(self, transaction):
        # KCB specific logic
        pass