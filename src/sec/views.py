from django.shortcuts import render, redirect
from sec.models import *
from django.http import HttpResponse

from sec.forms import *


def principal(request):
	return render(request, 'principal.html')

def add_pregunta(request):
	if request.method == 'POST':
		form = preguntaForm(request.POST)
		if form.is_valid():
			form.save()
		return redirect('principal')
	else:
		form = preguntaForm()

	return render(request, 'add_pregunta.html', {'form':form})

