from django.contrib import admin
from .models import Paciente, Doctor, Especialidad, DocEspe, Cita, AtencionMedica, HistoriaMedica, Farmacia

# Register your models here.

admin.site.register(Paciente)
admin.site.register(Doctor)
admin.site.register(Especialidad)
admin.site.register(DocEspe)
admin.site.register(Cita)
admin.site.register(AtencionMedica)
admin.site.register(HistoriaMedica)
admin.site.register(Farmacia)
