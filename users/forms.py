from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


class UserRegisterForm(UserCreationForm):
	username = forms.CharField(label="", required=True,
								  widget=forms.TextInput(
									  attrs={'placeholder': "Exemple@: Service",
											 'class': 'shadow-sm form-control', 'id': 'username', 'type': 'text',
											 'name': 'username'}))
	password1 = forms.CharField(label="Mot de passe", widget=forms.PasswordInput(
		attrs={'class': 'shadow-sm form-control', 'id': 'password', 'placeholder': 'Mot de passe',
			   'name': 'password'}),
							   required=True)
	password2 = forms.CharField(label="Confirmez votre mot de passe", widget=forms.PasswordInput(
		attrs={'class': 'shadow-sm form-control', 'id': 'confirmPassword',
			   'placeholder': 'Confirmez votre mot de passe', 'name': 'confirm_password'}), required=True)

	email = forms.CharField(label="", required=True, widget=forms.TextInput(
		attrs={'placeholder': "Exemple@: franck@gmail.com", 'type': 'email', 'class': 'shadow-sm form-control', 'id': 'email',
			   'name': 'email'}))

	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']


class UserForm(AuthenticationForm):
	username = forms.CharField(label="", required=True,
							   widget=forms.TextInput(
								   attrs={'placeholder': "Exemple@: Service",
										  'class': 'shadow-sm form-control', 'id': 'username', 'type': 'text',
										  'name': 'username'}))
	password = forms.CharField(label="Mot de passe", widget=forms.PasswordInput(
		attrs={'class': 'shadow-sm form-control', 'id': 'password', 'placeholder': 'Mot de passe',
			   'name': 'password'}), required=True)