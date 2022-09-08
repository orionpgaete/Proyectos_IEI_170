from django.shortcuts import render

# Create your views here.

def mitemplate(request):

    data = {"nombre" : "Pedro", "apellido": "Gaete"}
    return render(request, 'templateWEB/miplantilla.html', data)

def usuario(request):
    data = {"id": "123", "nombre": "Pedro Gaete", "email": "pedro@pedro.cl"}

    return render(request, 'templateWEB/userInfoTemplate.html', data)
