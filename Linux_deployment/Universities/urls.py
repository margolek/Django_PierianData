from django.urls import path
from . import views

app_name = 'Universities'

urlpatterns = [
	path('',views.IndexView.as_view(),name='index'),
	path('universities/',views.SchoolView.as_view(),name='school_list'),
	path('universities/<pk>/',views.SchoolViewDetail.as_view(),name='detail'),
	path('universities/create',views.SchoolViewCreate.as_view(),name='create'),
	path('universities/update/<pk>/',views.SchoolViewUpdate.as_view(),name='update'),
	path('universities/delete/<pk>/',views.SchoolViewDelete.as_view(),name='delete'),
]