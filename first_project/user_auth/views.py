from django.shortcuts import render
from user_auth.forms import UserForm, UserProfileInfoForm

from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect,HttpResponse
from django.urls import reverse
#If we ever want to views required login in
from django.contrib.auth.decorators import login_required


def index(request):
	return render(request, 'user_auth/index.html')

def register(request):

	registered = False

	if request.method == 'POST':
		user_form = UserForm(data=request.POST)
		profile_form = UserProfileInfoForm(data=request.POST)

		if user_form.is_valid() and profile_form.is_valid():

			user = user_form.save()
			user.set_password(user.password)
			user.save()

			profile = profile_form.save(commit=False)
			#One to One relationship
			profile.user = user

			if 'profile_pic' in request.FILES:
				#request.FILES will be albo used with csv,pdf etc.
				#'profile_pic' is a key of dictionary defined in models.py
				profile.profile_pic = request.FILES['profile_pic']
			profile.save()

			registered = True
		else:
			print(user_form.errors,profile_form.errors)
	else:
		user_form = UserForm()
		profile_form = UserProfileInfoForm()

	return render(request, 'user_auth/registration.html',
								{
								'user_form':user_form,
								'profile_form':profile_form,
								'registered':registered
								})

def user_login(request):

	if request.method == 'POST':
		#get username and password from login.html file
		username = request.POST.get('username')
		password = request.POST.get('password')

		#work with authentication built-in fnc
		user = authenticate(username=username,password=password)

		if user:
			if user.is_active:
				login(request, user)
				return HttpResponseRedirect(reverse('user_auth:index'))
			else:
				return HttpResponse("ACCOUNT NOT ACTIVE")
		else:
			print('Someone tried to login and failed!')
			print('Username: {} and password {}'.format(username,password))
			return HttpResponse("Invalid login details supplied!")
	else:
		return render(request, 'user_auth/login.html',{})

#User decorators in order to make sure that user who want to logout
#is the same user that log in
@login_required
def user_logout(request):
	logout(request)
	return HttpResponseRedirect(reverse('user_auth:index'))

#Special method created in order to confirm that
#login_required decorator work properly
@login_required
def special(request):
	return HttpResponse('You are log in, Awesone!')