from django.contrib import admin
from serialApp.models import Estudiante

# Register your models here.

class EstudianteAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'email', 'puntos']

admin.site.register(Estudiante, EstudianteAdmin)
