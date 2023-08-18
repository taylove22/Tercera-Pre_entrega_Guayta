from django.urls import path, include
from .views import *





urlpatterns = [
    path('', home, name="base"),
    
    path('Cursos/', cursos, name="Cursos"),
    path('estudiantes/', estudiantes, name="estudiantes"),
    path('Profesores/', profesores, name="profesores"),
    path('curso_form/', cursoForm, name="curso_form"),
    path('buscarcurso/', buscarcurso, name="buscarcurso"),
    path('buscar2/', buscar2, name="buscar2"),

]

