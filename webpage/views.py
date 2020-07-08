# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
def home(request):
	return render(request, 'home.html')

def about_us(request):
	return render(request, 'about-us.html')

def lawyers(request):
	return render(request, 'asesores.html')

def services(request):
	return render(request, 'servicios.html')

def consulting(request):
	return render(request, 'consulta-legal.html')

def courses(request):
	return render(request, 'cursos.html')

def contact_us(request):
	return render(request, 'contacto.html')

def online_consulting(request):
	return render(request, 'consulta-online48.html')