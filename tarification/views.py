from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.views import View
from .forms import SubscriptionForm, ContactForm
from .models import Subscription


@method_decorator(login_required, name='dispatch')
class SubscriptionView(View):
    plan = None
    template_name = None

    def get(self, request):
        form = SubscriptionForm(initial={'plan': self.plan})
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = SubscriptionForm(request.POST)
        if form.is_valid():
            subscription = form.save(commit=False)
            subscription.user = request.user
            subscription.save()
            return redirect('subscription_success')
        return render(request, self.template_name, {'form': form})

@method_decorator(login_required, name='dispatch')
class StandardSubscriptionView(SubscriptionView):
    plan = 'standard'
    template_name = 'tarification/standard_subscription.html'

@method_decorator(login_required, name='dispatch')
class FamilyRestrictedSubscriptionView(SubscriptionView):
    plan = 'family_restricted'
    template_name = 'tarification/family_restricted_subscription.html'

@method_decorator(login_required, name='dispatch')
class FamilyExtendedSubscriptionView(SubscriptionView):
    plan = 'family_extended'
    template_name = 'tarification/family_extended_subscription.html'


def home(request):
    return render(request, 'tarification/index.html')


def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()  # Enregistre le message dans la base de données
            return redirect('contact_success')
    else:
        form = ContactForm()

    return render(request, 'tarification/contacts.html', {'form': form})

def contact_success(request):
    return render(request, 'tarification/contact_success.html')