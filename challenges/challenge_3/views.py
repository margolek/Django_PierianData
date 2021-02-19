from django.shortcuts import render
from challenge_3.models import User
from . import forms

def index(request):

	return render(request, 'challenge_3/index.html')


def users(request):
	user_list = User.objects.order_by('first_name')
	my_dict = {
		'user_access':user_list
	}
	return render(request, 'challenge_3/users.html',context=my_dict)

def usersform(request):
	form = forms.UserForm(request.POST)

	if request.method == 'POST':
		form.save()	
		return index(request)
	return render(request, 'challenge_3/usersform.html',{'form':form})
