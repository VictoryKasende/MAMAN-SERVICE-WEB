from django.urls import path
from django.views.generic import TemplateView

from .views import (
    StandardSubscriptionView,
    FamilyRestrictedSubscriptionView,
    FamilyExtendedSubscriptionView,
    home,
    contact_view,
    contact_success
)
urlpatterns = [
    path('', home, name='index'),
    path('contact/', contact_view, name='contact'),
    path('contact/success/', contact_success, name='contact_success'),
    path('standard/', StandardSubscriptionView.as_view(), name='standard_subscription'),
    path('family-restricted/', FamilyRestrictedSubscriptionView.as_view(), name='family_restricted_subscription'),
    path('family-extended/', FamilyExtendedSubscriptionView.as_view(), name='family_extended_subscription'),
    path('success/', TemplateView.as_view(template_name='tarification/subscription_success.html'), name='subscription_success'),
]