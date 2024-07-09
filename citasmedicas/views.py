from django.shortcuts import render
from django.http import HttpResponse

from rest_framework import viewsets
from .serializer import PacienteSerializer, DoctorSerializer, EspecialidadSerializer, DocEspeSerializer, CitaSerializer, AtencionMedicaSerializer, HistoriaMedicaSerializer, FarmaciaSerializer
from .models import Paciente, Doctor, Especialidad, DocEspe, Cita, AtencionMedica, HistoriaMedica, Farmacia

# Llamar a los templates
def index(request):                                          #nombre será el que se llame en la urls views.index 
    title='Portal de citas medicas'                          #una variable
    return render(request, 'home.html', {'title':title})     #llamo a la variable

def paciente(request):
    paciente = Paciente.objects.all()
    return render(request, 'paciente.html',{'paciente':paciente})

def doctor(request):
    doctor = Doctor.objects.all()
    return render(request, 'doctor.html',{'doctor':doctor})

def especialidad(request):
    especialidad = Especialidad.objects.all()
    return render(request, 'especialidad.html',{'especialidad':especialidad})

def docEspe(request):
    docEspe = DocEspe.objects.all()
    return render(request, 'docEspe.html',{'docEspe':docEspe})

def cita(request):
    cita = Cita.objects.all()
    return render(request, 'cita.html',{'cita':cita})

def atencionMedica(request):
    atencionMedica = AtencionMedica.objects.all()
    return render(request, 'atencionMedica.html',{'atencionMedica':atencionMedica})

def historiaMedica(request):
    historiaMedica = HistoriaMedica.objects.all()
    return render(request, 'historiaMedica.html',{'historiaMedica':historiaMedica})

def farmacia(request):
    farmacia = Farmacia.objects.all()
    return render(request, 'farmacia.html',{'farmacia':farmacia})

# Create your views here.
#vistas para el serializer

class PacienteView(viewsets.ModelViewSet):
    serializer_class = PacienteSerializer
    queryset = Paciente.objects.all()

class DoctorView(viewsets.ModelViewSet):
    serializer_class = DoctorSerializer
    queryset = Doctor.objects.all()

class EspecialidadView(viewsets.ModelViewSet):
    serializer_class = EspecialidadSerializer
    queryset = Especialidad.objects.all()

class DocEspeView(viewsets.ModelViewSet):
    serializer_class = DocEspeSerializer
    queryset = DocEspe.objects.all()

class CitaView(viewsets.ModelViewSet):
    serializer_class = CitaSerializer
    queryset = Cita.objects.all()

class AtencionMedicaView(viewsets.ModelViewSet):
    serializer_class = AtencionMedicaSerializer
    queryset = AtencionMedica.objects.all()

class HistoriaMedicaView(viewsets.ModelViewSet):
    serializer_class = HistoriaMedicaSerializer
    queryset = HistoriaMedica.objects.all()

class FarmaciaView(viewsets.ModelViewSet):
    serializer_class = FarmaciaSerializer
    queryset = Farmacia.objects.all()
