from django.shortcuts import render
from django.http import JsonResponse
from Api_Proyecto.models import Empleados

# Create your views here.

def verempleados(request):
    emp = {
        'id' : 123,
        'nombre': 'Pedro',
        'email': 'pedro@peyo.cl',
        'sueldo': '50000000000'
    }
    return JsonResponse(emp)

def verempleadosDb(request):
    empleado = Empleados.objects.all()
    data = {'empleados' : list(empleado.values('nombre', 'sueldo'))}

    return JsonResponse(data)