from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class University(models.Model):

	name = models.CharField(max_length=100,unique=True)
	url = models.URLField(max_length=100)
	email = models.EmailField(max_length=100)
	location = models.CharField(max_length=100)

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse('Universities:detail',kwargs={'pk':self.pk})


class Student(models.Model):

	first_name = models.CharField(max_length=100)
	last_name = models.CharField(max_length=100)
	school = models.ForeignKey(University, on_delete=models.CASCADE)

	def __str__(self):
		return self.first_name

