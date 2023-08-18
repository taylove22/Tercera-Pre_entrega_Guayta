from django.shortcuts import render
from .models import Curso
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'aplicacion/home.html')

def cursos(request):
    contexto = {'cursos': Curso.objects.all()}
    return render(request, 'aplicacion/cursos.html')

def profesores(request):
    return render(request, 'aplicacion/profesores.html')    

def estudiantes(request):
    return render(request, 'aplicacion/estudiantes.html') 



def cursoForm(request):
    if request.method == "POST":
        nombre = request.POST['nombre']
        comision = request.POST['comision']
        curso = Curso(nombre=nombre, comision=comision)
        curso.save()
        return HttpResponse("Se grabó con éxito")
    return render(request, "aplicacion/cursoform.html")

def buscarcurso(request):
    return render(request, "aplicacion/buscarcurso.html")

def buscar2(request):
    if request.GET['buscar']:
        patron = request.GET['buscar']
        cursos = Curso.objects.filter(nombre__icontains=patron)
        contexto = {"cursos": cursos}
        return render(request,'aplicacion/cursos.html', contexto)
    return HttpResponse("No se ingreso nada")    
   
