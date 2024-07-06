from django.contrib import admin
from .models import Subscription

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

admin.site.register(Subscription, SubscriptionAdmin)
