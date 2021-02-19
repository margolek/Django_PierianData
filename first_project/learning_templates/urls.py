from django.urls import path
from learning_templates import views

#TEMPLATE TAGGING
app_name = 'learning_templates'

urlpatterns = [
	path('',views.index,name='index'),
	path('relative/',views.relative,name='relative'),
	path('other/',views.other,name='other'),
]