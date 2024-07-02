from django.shortcuts import render
from django.http import HttpResponse

from rest_framework import viewsets
from .serializer import DoctoresSerializer, SintomasSerializer, CitaSerializer
from .models import Doctores, Sintomas, Cita
from django.shortcuts import render 

# Create your views here.

def principal(request):
    title='Portal de citas medicas'
    return render(request,'home.html', {'title':title})

def doctores(request):
    doctores = Doctores.objects.all()
    return render(request, 'doctores.html',{'doctores':doctores})

def about(request):
    return HttpResponse("<h2>About</h2>")

#las vistas para el serializer

class DoctoresView(viewsets.ModelViewSet):
	serializer_class = DoctoresSerializer
	queryset = Doctores.objects.all()

class SintomasView(viewsets.ModelViewSet):
	serializer_class = SintomasSerializer
	queryset = Sintomas.objects.all()

class CitaView(viewsets.ModelViewSet):
	serializer_class = CitaSerializer
	queryset = Cita.objects.all()
