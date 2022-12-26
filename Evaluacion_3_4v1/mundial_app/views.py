from os import stat
from django.shortcuts import render
from django.http import JsonResponse
from mundial_app.models import Equipo, Jugador
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated

from .serializers import EquipoSerializer, JugadorSerializer
from mundial_app import serializers
# Create your views here.

@permission_classes((AllowAny,))
def listaEquipo(request):
    equipo = Equipo.objects.all()
    data = {'equipo': equipo}
    return render(request, 'lista_Equipo.html', data)

def mostrarEquipo(request, id):
    equipo = Equipo.objects.filter(id=id).first()
    data = {'equipo': equipo}
    return render(request, 'muestra_equipo.html', data)