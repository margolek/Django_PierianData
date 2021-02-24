from django.db import models

class School(models.Model):
	name = models.CharField(max_length=100)
	principal = models.CharField(max_length=100)
	location = models.CharField(max_length=100)


	#String representation of our model
	def __str__(self):
		return self.name

class Student(models.Model):
	name = models.CharField(max_length=100)
	age = models.PositiveIntegerField()
	school = models.ForeignKey(School, related_name='students',
									   on_delete=models.CASCADE)

	def __str__(self):
		return self.name 
