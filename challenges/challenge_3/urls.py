from django.urls import path
from challenge_3 import views

urlpatterns = [
	path('',views.index,name='index'),
	path('users/',views.users,name='users'),
	path('usersform/',views.usersform,name='usersform'),
]