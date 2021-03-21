from django.contrib.auth import get_user_model
#https://docs.djangoproject.com/en/3.1/topics/auth/default/#django.contrib.auth.forms.UserCreationForm
from django.contrib.auth.forms import UserCreationForm

class UserCreateForm(UserCreationForm):

	class Meta:
		model = get_user_model()
		fields = ['username','email','password1','password2']

	def __init__(self, *args, **kwargs):
	    super().__init__(*args, **kwargs)
	    self.fields['username'].label = 'Display Name'
	    self.fields['email'].label = 'Email Address'