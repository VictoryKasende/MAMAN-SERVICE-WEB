from django.urls import path
from django.contrib.auth import views as auth_views
from .views import home, contact

urlpatterns = [
    path('', home, name='index'),
    path('contacts/', contact, name='contacts')
]