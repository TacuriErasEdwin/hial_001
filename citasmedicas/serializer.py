from rest_framework import serializers
from .models import Doctores, Sintomas, Cita

class DoctoresSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctores
        #fields:('id', 'nombre','apellido')
        fields = '__all__'

class SintomasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sintomas
        fields = '__all__'

class CitaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cita
        fields = '__all__'
