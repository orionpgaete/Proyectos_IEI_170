from django.shortcuts import render
from persona_APP.models import Persona

# Create your views here.

def listapersona(request):
    perso = Persona.objects.all()
    data = {'persona': perso}
    return render(request, 'empleados.html', data)
