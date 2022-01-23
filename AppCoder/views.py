from django.shortcuts import render, redirect
from AppCoder.models import Curso


# Create your views here.

from django.http import HttpResponse

from Red.Red.AppCoder.forms import CursoFormulario

def inicio(request):

   return render(request, 'AppCoder/inicio.html')

def cursos(request):

    return render(request, 'AppCoder/cursos.html', {"cursos": Curso.objects.all()})

def profesores(request):

    return HttpResponse ("vista profesores") 
def estudiantes(request):

    return HttpResponse ("vista estudiantes")
def entregable(request):

    return HttpResponse ("vista entregables")
def cursos_formularios(request):
    if request.method == "POST":
        formulario = CursoFormulario(request.POST)
        if formulario.is_valid(): 
            data = formulario.cleaned_data

            Curso.objects.create(nombre=data["curso"], camada=data["camada"])
            return redirect("cursos")
    else:
    
        formulario = CursoFormulario()
    return render(request, 'AppCoder/cursosFormularios.html')
