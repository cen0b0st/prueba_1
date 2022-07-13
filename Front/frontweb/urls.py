from django.urls import path
from frontweb import views

urlpatterns = [
    path('', views.home, name="Formulario de Solicitud o Reclamos"),
]