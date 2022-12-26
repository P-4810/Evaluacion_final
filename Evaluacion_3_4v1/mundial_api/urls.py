from django.contrib import admin
from django.urls import path
from .views import mostrarEquipo,gestionarJugador

urlpatterns = [
    path('equipo/<int:id>', mostrarEquipo),
    path('jugador/editar/<int:id>', gestionarJugador)
]