from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserForm(UserCreationForm):
	email = forms.EmailField()
	#Meta class keep configuration in one place
	class Meta():
		model = User
		fields = ['username','email','password1','password2']
