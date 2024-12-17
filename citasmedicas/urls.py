from django.urls import path, include
from . import views
from rest_framework import routers
from rest_framework.documentation import include_docs_urls

router=routers.DefaultRouter()
router.register(r'paciente', views.PacienteView,'paciente')
router.register(r'doctor', views.DoctorView,'doctor')
router.register(r'especialidad', views.EspecialidadView,'especialidad')
router.register(r'docEspe', views.DocEspeView,'docEspe')
router.register(r'cita', views.CitaView,'cita')
router.register(r'atencionMedica', views.AtencionMedicaView,'atencionMedica')
router.register(r'historiaMedica', views.HistoriaMedica,'historiaMedica')
router.register(r'farmacia', views.Farmacia,'farmacia')

urlpatterns = [
    path('home/',views.index), #dentro de home se encuentra index
    path('about/',views.about ),
    path("paciente/",views.paciente ),
    path("doctor/",views.doctor, name= 'doctor' ),
    path("especialidad/",views.especialidad, name= 'especialidad' ),
    path("docEspe/",views.docEspe ),
    path("cita/",views.cita ),
    path("atencionMedica/",views.atencionMedica ),
    path("historiaMedica/",views.historiaMedica ),
    path("farmacia/",views.farmacia ),

    #para acceder a las URL de la nuestra aplicación con inicio de sesión
    path('login/', views.user_login, name='login'),
    path('signup/', views.user_signup, name='signup'),
    path('logout/', views.user_logout, name='logout'),

    #para acceder a las URL de los form recien creados
    path("nuevodoctor/",views.NuevoDoc, name='nuevodoctor' ),
    path("nuevopaciente/",views.NuevoPa, name='nuevopaciente' ),
    path("nuevoespecialidad/",views.NuevoEspe, name='nuevoespecialidad' ),
]
