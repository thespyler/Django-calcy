from django.contrib import admin
from django.urls import path
from add.views import *	

urlpatterns = [
	path('form/', hello),
	path('', add)
]