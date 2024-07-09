from rest_framework import serializers
from .models import Paciente, Doctor, Especialidad, DocEspe, Cita, AtencionMedica, HistoriaMedica, Farmacia

class PacienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paciente
        fields = '__all__'

class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = '__all__'

class EspecialidadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Especialidad
        fields = '__all__'

class DocEspeSerializer(serializers.ModelSerializer):
    class Meta:
        model = DocEspe
        fields = '__all__'

class CitaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cita
        fields = '__all__'

class AtencionMedicaSerializer(serializers.ModelSerializer):
    class Meta:
        model = AtencionMedica
        fields = '__all__'

class HistoriaMedicaSerializer(serializers.ModelSerializer):
    class Meta:
        model = HistoriaMedica
        fields = '__all__'

class FarmaciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Farmacia
        fields = '__all__'



