from django.urls import path
from challenge_2 import views

urlpatterns = [
	path('',views.help,name='help'),
]