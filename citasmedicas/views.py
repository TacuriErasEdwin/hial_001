from django.shortcuts import render

from rest_framework import viewsets
from .serializer import DoctoresSerializer, SintomasSerializer, CitaSerializer 
from .models import Doctores, Sintomas, Cita
# Create your views here.


class Doctoresview(viewsets.ModelViewSet):
	serializer_class = DoctoresSerializer
	queryset = Doctores.objects.all()

class Sintomasview(viewsets.ModelViewSet):
	serializer_class = SintomasSerializer
	queryset = Sintomas.objects.all()

class Citaview(viewsets.ModelViewSet):
	serializer_class = CitaSerializer
	queryset = Cita.objects.all()
