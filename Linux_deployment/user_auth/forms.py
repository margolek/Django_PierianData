from django import forms
from django.contrib.auth.models import User
from user_auth.models import UserProfileSite

class UserForm(forms.ModelForm):

	class Meta():
		model = User
		fields = ('username','password')

class UserProfileSiteForm(forms.ModelForm):

	class Meta():
		model = UserProfileSite
		fields = ('profile_pic')