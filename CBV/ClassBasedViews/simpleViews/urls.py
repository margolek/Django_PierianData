from django.urls import path
from simpleViews import views

app_name = 'simpleViews'

urlpatterns = [
	path('',views.SchoolListView.as_view(),name='list'),
	path('<pk>/',views.SchoolDetailView.as_view(),name='detail'),
]
