from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.views import View
from .forms import UserRegisterForm, UserForm
from django.urls import reverse_lazy


class RegisterView(View):
    def get(self, request):
        form = UserRegisterForm()
        return render(request, 'users/register.html', {'form': form})

    def post(self, request):
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            return render(request, 'users/register.html', {'form': form})


class CustomLoginView(LoginView):
    template_name = 'users/login.html'
    authentication_form = UserForm
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('index')  # Remplacez 'home' par le nom de votre page d'accueil ou de redirection après connexion