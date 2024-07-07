from django import forms
from .models import Subscription, ContactMessage


class SubscriptionForm(forms.ModelForm):
    class Meta:
        model = Subscription
        fields = ['account_number', 'plan']
        widgets = {
            'account_number': forms.TextInput(attrs={'class': 'form-control'}),
            'plan': forms.HiddenInput(),
        }


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'shadow form-control', 'placeholder': 'Name', 'required': True}),
            'email': forms.EmailInput(attrs={'class': 'shadow form-control', 'placeholder': 'Email', 'required': True}),
            'message': forms.Textarea(attrs={'class': 'shadow form-control', 'rows': 6, 'placeholder': 'Message', 'required': True}),
        }

class PaymentForm(forms.Form):
    amount = forms.DecimalField(max_digits=10, decimal_places=2)
    phone_number = forms.CharField(max_length=15, help_text="Entrez votre numéro de mobile money")