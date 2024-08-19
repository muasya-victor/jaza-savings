class PaymentGateway:
    def create_payment(self, transaction):
        raise NotImplementedError

    def execute_payment(self, transaction, **kwargs):
        raise NotImplementedError('Subclasses must implement this method')

    def cancel_payment(self, transaction):
        raise NotImplementedError
