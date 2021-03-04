from django.shortcuts import render,redirect
from django.contrib import messages
from user_auth.forms import UserForm
from django.contrib.auth.decorators import login_required


def index(request):
	return render(request, 'user_auth/index.html')


def register(request):
	if request.method == 'POST':
		form = UserForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			messages.success(request, f'Account created for {username}')
			return redirect('user_auth:login')
	else:
		form = UserForm()
	return render(request, 'user_auth/registration.html',{'form':form})

@login_required
def profile(request):
	return render(request, 'user_auth/profile.html')
