from django.contrib import admin
from .models import Doctores, Sintomas, Cita

# Register your models here.
admin.site.register(Doctores)
admin.site.register(Sintomas)
admin.site.register(Cita)
