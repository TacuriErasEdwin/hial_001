form django.shorcuts import render

from rest_framework import viewsets
from .serializer import DoctoresSerializer, SintomasSerializer, CitaSerializer
from .models import Doctores, Sintomas, Cita

#Create your views here.

class Doctoresview(viewsets.ModelViewSet);
	serializer_class = DoctoresSerializer
	queryset = Doctores.objects.all()

class Sintomasview(viewsets.ModelViewSet);
	serializer_class = SintomasSerializer
	queryset = Sintomas.objects.all()

class Citasview(viewsets.ModelViewSet);
	serializer_class = CitasSerializer
	queryset = Citas.objects.all()
