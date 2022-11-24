from django.shortcuts import render
from .serializers import EstudiantesSerializer
from .models import Estudiante
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

# Create your views here.

@api_view(['GET', 'POST'])
def estudiante_list(request):
    if request.method == 'GET':
        estu = Estudiante.objects.all()
        serial = EstudiantesSerializer(estu, many=True)
        return Response(serial.data)
    
    if request.method == 'POST':
        serial = EstudiantesSerializer(data = request.data)
        if serial.is_valid():
            serial.save()
            return Response(serial.data, status=status.HTTP_201_CREATED)
        return Response(serial.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def estudiante_detalle(request, pk):
    try:
        estu = Estudiante.objects.get(id = pk)
    except Estudiante.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serial = EstudiantesSerializer(estu)
        return Response(serial.data)

    if request.method == 'PUT':
        serial = EstudiantesSerializer(estu, data=request.data)
        if serial.is_valid():
            serial.save()
            return Response(serial.data)
        return Response(serial.errors, status=status.HTTP_400_BAD_REQUEST)
        
    if request.method == 'DELETE':
        estu.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)






