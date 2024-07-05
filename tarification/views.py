from django.shortcuts import render


def home(request):
    return render(request, 'tarification/index.html')


def contact(request):
    return render(request, 'tarification/contacts.html')