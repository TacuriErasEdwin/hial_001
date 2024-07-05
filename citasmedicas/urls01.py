from django.urls import path, include
from . import views
from rest_framework import routers
from rest_framework.documentation import include_docs_urls

router=routers.DefaultRouter()
router.register(r'pacientes', views.PacientesView,'pacientes')
router.register(r'medicos', views.MedicosView,'medicos')
router.register(r'especialidades', views.EspecialidadesView,'especialidades')
router.register(r'citas', views.CitasView,'citas')
router.register(r'consulta_medica', views.Consulta_medicaView,'consulta_medica')
router.register(r'historia_clinica', views.Historia_clinicaView,'historia_clinica')

urlpatterns = [
    path("home/",views.index ),
    path("pacientes/",views.pacientes ),
    path("medicos/",views.medicos ),
    path("especialidades/",views.especialidades ),
    path("citas/",views.citas ),
    path("consulmed/",views.consulmed ),
    path("historia/",views.historia ),
    path("api/",include(router.urls) ),
    path("docsapi/",include_docs_urls(title='Citas Medicas API V1') ), 
]
