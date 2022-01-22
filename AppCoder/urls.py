

from django.urls import path
from AppCoder.views import prueba_template, ver_curso, crear_curso

urlpatterns = [
    
    path('ver/', ver_curso),
    path('crear/', crear_curso),
    path('template/', prueba_template),
]
