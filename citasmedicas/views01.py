from django.shortcuts import render
from django.http import HttpResponse

from rest_framework import viewsets
from .serializer import PacientesSerializer, MedicosSerializer, EspecialidadesSerializer, CitasSerializer, Consulta_medicaSerializer, Historia_clinicaSerializer
from .models import Pacientes, Medicos, Especialidades, Citas, Consulta_medica, Historia_clinica

# Llamar a los templates

def index(request):    #nombre será el que se llame en la urls views.index 
    title='Portal de citas medicas' #una variable
    return render(request, 'home.html', {'title':title}) #llamo a la variable

def pacientes(request):
    pacientes = Pacientes.objects.all()
    return render(request, 'pacientes.html',{'pacientes':pacientes})

def medicos(request):
    medicos = Medicos.objects.all()
    return render(request, 'medicos.html',{'medicos':medicos})

def especialidades(request):
    especialidades = Especialidades.objects.all()
    return render(request, 'especialid.html',{'especialidades':especialidades})

def citas(request):
    citas = Citas.objects.all()
    return render(request, 'especialid.html',{'citas':citas})

def consulmed(request):
    consulmed = Consulta_medica.objects.all()
    return render(request, 'consulmed.html',{'Consulta_medica':consulmed})

def historia(request):
    historia = Historia_clinica.objects.all()
    return render(request, 'historia.html',{'Historia_clinica':historia})

#vistas para el serializer

class PacientesView(viewsets.ModelViewSet):
    serializer_class = PacientesSerializer
    queryset = Pacientes.objects.all()

class MedicosView(viewsets.ModelViewSet):
    serializer_class = MedicosSerializer
    queryset = Medicos.objects.all()

class EspecialidadesView(viewsets.ModelViewSet):
    serializer_class = EspecialidadesSerializer
    queryset = Especialidades.objects.all()

class CitasView(viewsets.ModelViewSet):
    serializer_class = CitasSerializer
    queryset = Citas.objects.all()

class Consulta_medicaView(viewsets.ModelViewSet):
    serializer_class = Consulta_medicaSerializer
    queryset = Consulta_medica.objects.all()

class Historia_clinicaView(viewsets.ModelViewSet):
    serializer_class = Historia_clinicaSerializer
    queryset = Historia_clinica.objects.all()
