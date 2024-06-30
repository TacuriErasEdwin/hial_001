from rest_framework import serializer
from .models import Doctores, Sintomas, Cita


class DoctoresSerializer (serializer.ModelsSerializer):
	class Meta:
		model = Doctores
		#fields:('id','nombre')
		field = '_all_'

class SintomasSerializer (serializer.ModelsSerializer):
	class Meta:
		model = Sintomas
		field = '_all_'

class CitaSerializer (serializer.ModelsSerializer):
	class Meta:
		model = Cita
		field = '_all_'
