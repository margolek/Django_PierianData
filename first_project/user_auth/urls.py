from django.urls import path
from user_auth import views

#Template URLS
app_name = 'user_auth'

urlpatterns = [
	path('',views.index,name='index'),
	path('registration/',views.register,name='register'),
	path('logout/',views.user_logout,name='logout'),
	path('special/',views.special,name='special'),
	path('login/',views.user_login,name='user_login'),
]