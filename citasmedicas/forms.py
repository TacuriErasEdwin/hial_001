from django import forms 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Paciente, Doctor, Especialidad, DocEspe, Cita, AtencionMedica, HistoriaMedica, Farmacia


class SignupForm(UserCreationForm):
    class Meta:
        model = User 
        fields = ['username', 'password1', 'password2']

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class NuevoDoctorModelForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = '__all__'

class NuevoPacienteModelForm(forms.ModelForm):
    class Meta:
        model = Paciente
        fields = '__all__'

class NuevoEspecialidadodelForm(forms.ModelForm):
    class Meta:
        model = Especialidad
        fields = '__all__'

class NuevoCitaodelForm(forms.ModelForm):
    class Meta:
        model = Cita
        fields = '__all__'

class NuevoAtencionModelForm(forms.ModelForm):
    class Meta:
        model = AtencionMedica
        fields = '__all__'

class NuevoHistoriaModelForm(forms.ModelForm):
    class Meta:
        model = HistoriaMedica
        fields = '__all__'

class NuevoFarmaciaModelForm(forms.ModelForm):
    class Meta:
        model = Farmacia
        fields = '__all__'
