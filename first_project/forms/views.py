from django.shortcuts import render
from . import forms
# Create your views here.

def index(request):
	return render(request, 'forms/index.html')

def form_name_view(request):
	form = forms.FormName()

	if request.method == 'POST':
		form = forms.FormName(request.POST)

	return render(request, 'forms/form_page.html',{'form':form})