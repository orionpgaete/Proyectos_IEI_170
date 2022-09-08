from django.http import HttpResponse
from django.template import Template, Context
import datetime

class Persona(object):
    def __init__(self, nombre, apellido) :
        self.nombre = nombre
        self.apellido = apellido

def web(request):
    #nombre = "Pedro"
    #apellido = "Gaete"
    ahora = datetime.datetime.now()

    p1=Persona("Profesor Pedro", "Gaete")


    
    doc_externo = open("D:/1. Clases INACAP/2. Clases/2.31 Programacion Back-End/Proyectos-IEI-170/proyecto2/proyecto2/html/miplantilla.html")

    plantilla = Template(doc_externo.read())

    doc_externo.close()

    conte = Context({"nom_persona":p1.nombre, "apel_persona":p1.apellido, "fecha": ahora, "temas":["Plantillas", "Modelos", "Formulario", "Vistas", "Despliegue"]})

    docu = plantilla.render(conte)

    return HttpResponse(docu)