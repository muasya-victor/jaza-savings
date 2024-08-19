from django.contrib import admin
from .models import Transaction


class TransactionAdmin(admin.ModelAdmin):
    list_display = ('user', 'amount', 'currency', 'payment_gateway', 'status', 'created_at', 'updated_at')
    list_filter = ('payment_gateway', 'status', 'currency')
    search_fields = ('user__username', 'gateway_transaction_id', 'description')
    ordering = ('-created_at',)


admin.site.register(Transaction, TransactionAdmin)
