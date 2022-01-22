import imp
from unittest import loader
from django.shortcuts import render
from django.http import HttpResponse
from .models import Curso
from django.template import loader
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

def prueba_template(request):
    # template = loader.get_template('Appcoder/index.html')
    # documento = template.render({})
    # return HttpResponse(documento)
    return render(request, 'Appcoder/index.html',{})