from django.db import models
from django.urls import reverse

class School(models.Model):
	name = models.CharField(max_length=100)
	principal = models.CharField(max_length=100)
	location = models.CharField(max_length=100)


	#String representation of our model
	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse('simpleViews:detail',kwargs={'pk':self.pk})

class Student(models.Model):
	name = models.CharField(max_length=100)
	age = models.PositiveIntegerField()
	school = models.ForeignKey(School, related_name='students',
									   on_delete=models.CASCADE)

	def __str__(self):
		return self.name 
