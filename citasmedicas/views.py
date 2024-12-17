from django.shortcuts import render
from django.http import HttpResponse

from rest_framework import viewsets
from .serializer import PacienteSerializer, DoctorSerializer, EspecialidadSerializer, DocEspeSerializer, CitaSerializer, AtencionMedicaSerializer, HistoriaMedicaSerializer, FarmaciaSerializer
from .models import Paciente, Doctor, Especialidad, DocEspe, Cita, AtencionMedica, HistoriaMedica, Farmacia
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout 
from .forms import SignupForm, LoginForm, NuevoDoctorModelForm, NuevoPacienteModelForm, NuevoEspecialidadodelForm,NuevoCitaodelForm, NuevoAtencionModelForm, NuevoHistoriaModelForm, NuevoFarmaciaModelForm

# Llamar a los templates
def index(request):                                          #nombre será el que se llame en la urls views.index 
    
    return render(request, 'home.html')     #llamo a la variable
    doctor = Doctor.objects.all()
def about(request):
    return render(request, 'about.html')   

def paciente(request):
    paciente = Paciente.objects.all()
    return render(request, 'paciente.html',{'paciente':paciente})

def doctor(request):
    doctor = Doctor.objects.all()
    return render(request, 'doctor.html',{'doctor':doctor})   #voy a enviar una variable a doctores html

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



# signup page
def user_signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form': form})

# login page
def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)    
                return redirect('/home/')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

# logout page
def user_logout(request):
    logout(request)
    return redirect('login')

#llamar a los forms
def NuevoDoc(request):
    form = NuevoDoctorModelForm()
    if request.method == 'POST':
        form = NuevoDoctorModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/home/')
    else:
        form = NuevoDoctorModelForm()
    return render(request, 'nuevodoctor.html', {'form': form})

def NuevoPa(request):
    form = NuevoPacienteModelForm()
    if request.method == 'POST':
        form = NuevoPacienteModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/home/')
    else:
        form = NuevoPacienteModelForm()
    return render(request, 'nuevopaciente.html', {'form': form})

def NuevoEspe(request):
    form = NuevoEspecialidadodelForm()
    if request.method == 'POST':
        form = NuevoEspecialidadodelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/home/')
    else:
        form = NuevoEspecialidadodelForm()
    return render(request, 'nuevoespecialidad.html', {'form': form})


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
