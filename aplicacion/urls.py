from django.urls import path, include
from .views import index, saludo, extra

urlpatterns = [
    #URLS DE APLICACION
    path('',index,name='index'),
    path('saludo/',saludo,name="saludo"),
    path('extra/',extra,name='extra'),
]