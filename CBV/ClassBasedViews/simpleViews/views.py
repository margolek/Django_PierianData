from django.shortcuts import render
from django.views.generic import View,TemplateView,ListView,DetailView
from . import models

class IndexView(TemplateView):
	template_name = 'index.html'

class SchoolListView(ListView):
	#Define own context object name
	context_object_name = 'schools'
	model = models.School

class SchoolDetailView(DetailView):
	context_object_name = 'school_detail'
	model = models.School
	template_name = 'simpleViews/school_detail.html'