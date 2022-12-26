from django.shortcuts import render
from django.contrib.auth import authenticate, logout
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import status
from rest_framework.response import Response

from mundial_app.serializers import EquipoSerializer,JugadorSerializer
from mundial_app.models import Equipo,Jugador



# Create your views here.
@csrf_exempt
@api_view(['POST'])
@permission_classes((AllowAny,))
def login(request):
    username = request.data.get('username')
    password = request.data.get('password')
    if username is None or password is None:
        return Response ({'error': 'Por favor ingrese usuario y/o contraseña en conjunto'}, status=status.HTTP_400_BAD_REQUEST)
    #intentar hacer login con los datos de la BD
    user = authenticate(username=username, password=password)

    if not user:
        return Response ({'error': 'Credenciales no válidas'}, status=status.HTTP_404_NOT_FOUND)

    token, _ = Token.objects.get_or_create(user=user)
    return Response ({'token': token.key}, status=status.HTTP_200_OK)

# mostar equipo
@csrf_exempt
@api_view(['GET'])
@permission_classes((IsAuthenticated,))
def mostrarEquipo(request, id):
    try:
        equipoc = Jugador.objects.get(equipo=id)
        serializado = JugadorSerializer(equipoc)
        return Response(serializado.data)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)


@csrf_exempt
@api_view(['PATCH', 'DELETE', 'POST'])
@permission_classes((IsAuthenticated,))
def gestionarJugador(request, id):
    #modificar
    if request.method == 'PATCH':
        try:
            jugador = Jugador.objects.get(id=id)
            serializador = JugadorSerializer(jugador, data=request.data, partial=True)
            if serializador.is_valid():
                serializador.save()
                return Response(status=status.HTTP_201_CREATED)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)

        return Response(serializador.errors, status=status.HTTP_400_BAD_REQUEST)
    
    #si deseo eliminar músico
    if request.method == 'DELETE':
        #hago eliminación
        try:
            jugador = Jugador.objects.get(id=id)
            jugador.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
        

    #ingresar
    if request.method == 'POST':
        try:
            serializador = JugadorSerializer(data=request.data)
            if serializador.is_valid():
                serializador.save()
                return Response(serializador.data, status=status.HTTP_201_CREATED)
            else:
                return Response(serializador.errors, status=status.HTTP_400_BAD_REQUEST)    
        except:
            return Response(serializador.errors, status=status.HTTP_400_BAD_REQUEST)