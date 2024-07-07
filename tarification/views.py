import time
from datetime import timedelta

from django.db import IntegrityError
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.utils import timezone
from django.utils.decorators import method_decorator
from django.views import View
from .forms import SubscriptionForm, ContactForm
from .models import Subscription
import uuid
from .forms import PaymentForm
from .models import Transaction
from cinetpay_sdk.s_d_k import Cinetpay
from django.conf import settings

@login_required
def payment_view(request, subscription_id):
    subscription = get_object_or_404(Subscription, id=subscription_id, user=request.user)
    amount = subscription.price

    if request.method == "POST":
        client = Cinetpay(settings.CINETPAY_API_KEY, settings.CINETPAY_SITE_ID)
        data = {
            'amount': amount,
            'currency': "USD",
            'transaction_id': f"TXN_{subscription.id}_{int(time.time())}",
            'description': f"Payment for {subscription.plan} plan",
            'return_url': request.build_absolute_uri(reverse('payment_success')),
            'notify_url': request.build_absolute_uri(reverse('payment_notify')),
            'customer_name': request.user.first_name,
            'customer_surname': request.user.email,
        }
        response = client.PaymentInitialization(data)
        if response['code'] == '201':
            transaction = Transaction.objects.create(
                user=request.user,
                subscription=subscription,
                transaction_id=response['data']['payment_token'],
                payment_token=response['data']['payment_token'],
                payment_url=response['data']['payment_url'],
                amount=amount,
                currency="USD"
            )
            return redirect(transaction.payment_url)
        else:
            return render(request, 'tarification/payment_error.html',
                          {'error': 'Payment initiation failed: ' + response['description']})

    return render(request, 'tarification/payment.html', {'subscription': subscription, 'amount': amount})

def payment_success(request):
    return render(request, 'tarification/payment_success.html')

def cinetpay_notify(request):
    if request.method == 'POST':
        data = request.POST
        transaction_id = data.get('transaction_id')
        status = data.get('status')
        try:
            transaction = Transaction.objects.get(transaction_id=transaction_id)
            transaction.status = status
            transaction.save()
        except Transaction.DoesNotExist:
            pass
    return HttpResponse(status=200)

@login_required
def subscribe(request, plan):
    plans = {
        'standard': 5.00,
        'family_restricted': 10.00,
        'family_extended': 15.00,
    }
    if plan not in plans:
        return redirect('plans')
    price = plans[plan]

    subscription, created = Subscription.objects.get_or_create(
        user=request.user,
        plan=plan,
        defaults={'price': price}
    )

    if not created:
        if subscription.end_date > timezone.now():
            subscription.end_date += timedelta(days=30)
        else:
            subscription.end_date = timezone.now() + timedelta(days=30)
    else:
        subscription.end_date = timezone.now() + timedelta(days=30)

    subscription.save()

    return redirect('payment', subscription_id=subscription.id)

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

