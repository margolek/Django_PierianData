from django.urls import path
from simpleViews import views

app_name = 'simpleViews'

urlpatterns = [
	path('',views.SchoolListView.as_view(),name='list'),
	path('<pk>/',views.SchoolDetailView.as_view(),name='detail'),
	path('simpleViews/create/',views.SchoolCreateView.as_view(),name='create'),
	path('simpleViews/update/<pk>/',views.SchoolUpdateView.as_view(),name='update'),
	path('simpleViews/delete/<pk>/',views.SchoolDeleteView.as_view(),name='delete'),
]
