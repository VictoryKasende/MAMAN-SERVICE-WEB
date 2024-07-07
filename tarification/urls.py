from django.urls import path
from django.views.generic import TemplateView

from .views import (
    home,
    contact_view,
    contact_success,
    payment_success,
    cinetpay_notify,
    subscribe,
    payment_view
)
urlpatterns = [
    path('', home, name='index'),
    path('contact/', contact_view, name='contact'),
    path('contact/success/', contact_success, name='contact_success'),
    path('success/', TemplateView.as_view(template_name='tarification/subscription_success.html'), name='subscription_success'),

    path('payment_success/', payment_success, name='payment_success'),
    path('cinetpay_notify/', cinetpay_notify, name='payment_notify'),
    path('payment/<int:subscription_id>/', payment_view, name='payment'),
    path('subscribe/<str:plan>/', subscribe, name='subscribe'),
]