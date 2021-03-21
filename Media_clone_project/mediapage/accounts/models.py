from django.db import models
from django.contrib import auth

#https://docs.djangoproject.com/en/3.1/topics/auth/default/
class User(auth.models.User,auth.models.PermissionsMixin):

	def __str__(self):
		return '@{}'.format(self.username)
