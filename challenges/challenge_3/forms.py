from django.forms import ModelForm
from challenge_3.models import User

# Create the form class.
class UserForm(ModelForm):
	class Meta:
		model = User
		fields = '__all__'

# Creating a form to add an user.
form = UserForm()

# Creating a form to change an existing user.
user = User.objects.get(pk=1)
form = UserForm(instance=user)