from django.contrib import admin
from .models import Subscription, Transaction, ContactMessage

class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ('account_number', 'plan', 'user', 'created_at')
    list_filter = ('plan', 'created_at')
    search_fields = ('account_number', 'user__username')
    ordering = ('-created_at',)

    fieldsets = (
        (None, {
            'fields': ('account_number', 'plan', 'user')
        }),
        ('Dates', {
            'fields': ('created_at',),
        }),
    )
    readonly_fields = ('created_at',)

class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'created_at')
    search_fields = ('name', 'email')
    list_filter = ('created_at',)
    ordering = ('-created_at',)

class TransactionAdmin(admin.ModelAdmin):
    list_display = ('transaction_id', 'user', 'amount', 'currency', 'created_at')
    search_fields = ('transaction_id', 'user__username', 'user__email')
    list_filter = ('created_at', 'currency')
    ordering = ('-created_at',)
    readonly_fields = ('transaction_id', 'payment_token', 'payment_url', 'created_at')
    fieldsets = (
        (None, {
            'fields': ('user', 'subscription', 'transaction_id', 'payment_token', 'payment_url', 'amount', 'currency')
        }),
        ('Dates', {
            'fields': ('created_at',),
        }),
    )

admin.site.register(ContactMessage, ContactMessageAdmin)
admin.site.register(Transaction, TransactionAdmin)
admin.site.register(Subscription, SubscriptionAdmin)
