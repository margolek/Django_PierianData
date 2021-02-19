from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import Topic,Webpage,AccessRecord

def index(request):
	wepages_list = AccessRecord.objects.order_by('date')
	date_dict = {'access_records':wepages_list}
	my_dict = {
	'insert_me':'Insert variable from templates/index.html file'
	}
	return render(request, 'first_app/index.html',context=date_dict)