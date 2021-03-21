from django.shortcuts import render
from django.urls import reverse_lazy
from . import forms
from django.views.generic import (TemplateView,ListView,DetailView,
								  CreateView,UpdateView,DeleteView)

class SignUp(CreateView):
	form_class = forms.UserCreateForm
	success_url = reverse_lazy('login')
	template_name = 'accounts/signup.html'
