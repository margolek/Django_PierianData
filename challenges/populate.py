import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','challenges.settings')

import django
django.setup()

from challenge_3.models import User
#Import library to work with dummy data
from faker import Faker
fakegen = Faker()

def populate(N=10):
	#Create fake data for User model
	for pop in range(N):
		fake_first = fakegen.first_name()
		fake_last = fakegen.last_name()
		fake_email = fakegen.email()

		#Set up data to User model
		user_model = User.objects.get_or_create(first_name=fake_first,
			last_name=fake_last,email=fake_email)[0]

if __name__ == '__main__':
	populate(10)
	print('Database update!')