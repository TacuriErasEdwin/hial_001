from django.urls import path, include
from . import views
from rest_framework import routers
from rest_framework.documentation import include_docs_urls

router=routers.DefaultRouter()
router.register(r'doctores', views.DoctoresView, 'doctores')
router.register(r'sintomas', views.SintomasView, 'sintomas')
router.register(r'cita', views.CitaView, 'cita')

urlpatterns = [
    path('home/',views.principal ),
    #path('about/',views.about ),
    path('doctores/',views.doctores ),
    path('api/v1',include(router.urls) ),
   # path('docsapi/',include_docs_urls(title='Citas Medicas API V2') ),
]
