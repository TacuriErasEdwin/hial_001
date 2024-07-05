from rest_framework import serializers
from .models import Pacientes, Medicos, Especialidades, Citas, Consulta_medica, Historia_clinica

class PacientesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pacientes
        fields = '_all_'

class MedicosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medicos
        fields = '_all_'

class EspecialidadesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Especialidades
        fields = '_all_'

class CitasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Citas
        fields = '_all_'

class Consulta_medicaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Consulta_medica
        fields = '_all_'

class Historia_clinicaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Historia_clinica
        fields = '_all_'
