from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def inicio(request):

    return HttpResponse ("vista inicio")
def cursos(request):

    return HttpResponse ("vista curso")
def profesores(request):

    return HttpResponse ("vista profesores") 
def estudiantes(request):

    return HttpResponse ("vista estudiantes")
def entregable(request):

    return HttpResponse ("vista entregables")
