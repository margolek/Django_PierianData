from django.urls import path
from user_auth import views
from django.contrib.auth import views as auth_views

app_name = 'user_auth'

urlpatterns = [
	path('',views.index,name='index'),
	path('register/',views.register,name='register'),
	path('profile/',views.profile,name='profile'),
	path('login/',auth_views.LoginView.as_view(template_name='user_auth/login.html'),name='login'),
	path('logout/',auth_views.LogoutView.as_view(template_name='user_auth/logout.html'),name='logout'),
]