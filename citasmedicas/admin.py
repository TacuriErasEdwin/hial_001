# Register your models here.
from django.contrib import admin
from .models import Doctores, Sintomas, Cita

admin.site.register(Doctores)
admin.site.register(Sintomas)
admin.site.register(Cita)
