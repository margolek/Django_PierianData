from django.contrib import admin
#Importing Student and School classes
from simpleViews.models import School,Student

admin.site.register(School)
admin.site.register(Student)