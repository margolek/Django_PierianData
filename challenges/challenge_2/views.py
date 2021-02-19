from django.shortcuts import render

def help(request):
	my_dict = {
	'insert_tag' : 'Help Page'
	}
	return render(request, 'challenge_2/help.html',context=my_dict)