from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import View,TemplateView,ListView

class IndexView(TemplateView):
	template_name = 'user_auth/index.html'

def register(request):
	form = UserCreationForm()
	return render(request, 'user_auth/registration.html',{'form':form})
