from django.shortcuts import render
from django.http import HttpResponse

from rest_framework import viewsets
from .serializer import DoctoresSerializer, SintomasSerializer, CitaSerializer
from .models import Doctores, Sintomas, Cita
from django.shortcuts import render 

# Create your views here.


class DoctoresView(viewsets.ModelViewSet):
	serializer_class = DoctoresSerializer
	queryset = Doctores.objects.all()

class SintomasView(viewsets.ModelViewSet):
	serializer_class = SintomasSerializer
	queryset = Sintomas.objects.all()

class CitaView(viewsets.ModelViewSet):
	serializer_class = CitaSerializer
	queryset = Cita.objects.all()
