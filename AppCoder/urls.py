from django.urls import path
from AppCoder.views import cursos
from AppCoder.views import estudiantes, inicio, cursos_formularios


urlpatterns = [
    path("cursos/", cursos, name= "cursos"),
    path("", inicio),
    path("estudiantes/", estudiantes),
    path("inicio/", inicio),
    path("cursosFormulario/", cursos_formularios , name ="cursos_formulario")


]