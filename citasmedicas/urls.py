from django.urls import path, include
from . import views
from rest_framework import routers

urlpatterns = [
    path('api/v1/', include(router.urls)),   # atravez de esta ryta vamos a llamar a los elementos
    ]


/// 
			//instalamos en la consola:
pip install coreapi  	//instalamos toda la documentacion instlar automaticamente del api
