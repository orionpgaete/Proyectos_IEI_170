import datetime
from django.http import HttpResponse

doc = """<html>
            <body>
                <h1>Hola alumnos IEI 170, en nuestra primera clase de Django</h1>
            </body>
        </html>"""


def saludo(request):
    return HttpResponse(doc)

def despedida(request):
    return HttpResponse("Hasta la vista Bye Bye")

def muestrafecha(request):
    fecha_actual=datetime.datetime.now()
    return HttpResponse("""<html>
                            <body>
                                <h2>Fecha y Hora Actuales %s</h2>
                            </body>
                        </html>""" %fecha_actual)

def calcularEdad(request, agno, edad):
   # edadactual=18
    periodo = agno-2022
    edadfuturo = edad + periodo

    return HttpResponse("""<html>
                            <body>
                                <h2>En el año %s tendras %s años</h2>
                            </body>
                        </html>""" %(agno, edadfuturo))