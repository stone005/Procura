from django.contrib import admin
from django.urls import path

from .views import(
	pratica_list,
	pratica_create,
	)

urlpatterns = [
    path('', pratica_list, name='PList'),
    path('crea/', pratica_create),
]