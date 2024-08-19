# views.py

from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Transaction
from .serializers import TransactionSerializer
from .utils import PaymentGatewayFactory


class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

    @action(detail=True, methods=['post'])
    def create_payment(self, request, pk=None):
        transaction = self.get_object()
        gateway = PaymentGatewayFactory.get_gateway(transaction.payment_gateway)
        payment = gateway.create_payment(transaction)

        if payment:
            # Assuming 'payment' has an 'id' and redirect URL to be sent in the response
            approval_url = next(link.href for link in payment.links if link.rel == "approval_url")
            return Response({'approval_url': approval_url}, status=status.HTTP_200_OK)
        return Response({'error': 'Payment creation failed'}, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=['post'])
    def execute_payment(self, request, pk=None):
        transaction = self.get_object()
        payer_id = request.data.get('payer_id')
        payment_id = request.data.get('payment_id')
        gateway = PaymentGatewayFactory.get_gateway(transaction.payment_gateway)

        payment = gateway.execute_payment(transaction, payer_id=payer_id, payment_id=payment_id)
        if payment:
            return Response({'status': 'Payment executed successfully'}, status=status.HTTP_200_OK)
        return Response({'error': 'Payment execution failed'}, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=['post'])
    def cancel_payment(self, request, pk=None):
        transaction = self.get_object()
        gateway = PaymentGatewayFactory.get_gateway(transaction.payment_gateway)
        gateway.cancel_payment(transaction)

        return Response({'status': 'Payment cancelled successfully'}, status=status.HTTP_200_OK)
