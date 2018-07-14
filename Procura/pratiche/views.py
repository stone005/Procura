from django.shortcuts import render, redirect
from django.http import HttpResponse

from .forms import Praticaform
from .models import Pratica


def pratica_create(request):
	form = Praticaform(request.POST or None)
	context = {
		'form': form
	}
	return render(request, 'pratica_form.html', context)

def pratica_list(request):
	queryset = Pratica.objects.all()
	context = {
		'object_list': queryset,
		'title': 'Lista Pratiche'	
	}
	return render(request, 'home.html', context)

