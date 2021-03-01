from django.shortcuts import render
from django.views.generic import View,TemplateView

class IndexView(TemplateView):
	template_name = 'universities/index.html'

	def get_context_data(self,**kwargs):
		context = super().get_context_data(**kwargs)
		context['injectme'] = 'Welcome to index page!'
		return context
