from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (View,TemplateView,ListView,DetailView,
								CreateView,UpdateView,DeleteView)
from Universities.models import Student,University

class IndexView(TemplateView):
	template_name = 'universities/index.html'

	def get_context_data(self,**kwargs):
		context = super().get_context_data(**kwargs)
		context['injectme'] = 'Welcome to index page!'
		return context

class SchoolView(ListView):
	context_object_name = 'school_list'
	model = University

class SchoolViewDetail(DetailView):
	context_object_name = 'school_detail'
	model = University

class SchoolViewCreate(CreateView):
	fields = ('name','url','email','location')
	context_object_name = 'school_create'
	model = University
		
class SchoolViewUpdate(UpdateView):
	fields = ('name','url')
	context_object_name = 'school_update'
	model = University

class SchoolViewDelete(DeleteView):
	model = University
	success_url = reverse_lazy('Universities:school_list')

