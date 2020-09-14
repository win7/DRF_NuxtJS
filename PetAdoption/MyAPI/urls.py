from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from MyAPI import views

urlpatterns = [
	path('owners/', views.OwnerList.as_view()),
	path('owners/<int:pk>/', views.OwnerDetail.as_view()),

	path('pets/', views.PetList.as_view()),
	path('pets/<int:pk>/', views.PetDetail.as_view()),
]