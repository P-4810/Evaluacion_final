from django.urls import path

from mundial_app.views import mostrarEquipo , listaEquipo


urlpatterns = [
    path('equipos/', listaEquipo),
    path('equipo/<int:id>', mostrarEquipo)
]