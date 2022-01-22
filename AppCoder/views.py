from django.shortcuts import render
from django.http import HttpResponse
from .models import Curso
# Create your views here.

def crear_curso(request):
    curso = Curso(nombre='Prueba',camada=5 )
    curso.save()

    return HttpResponse(f'El curso es: {curso.nombre} y la camada es: {curso.camada} ')

def ver_curso(request):
    cursos = Curso.objects.all()

    texto = ''
    for curso in cursos:
        texto += f'Curso: {curso.nombre} <br>'
    cursos = cursos.last()

    return HttpResponse(f'{texto}')