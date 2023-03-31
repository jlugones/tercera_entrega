from django.urls import path, include
from AppCoder1 import views

from AppCoder1.views import curso, estudiante, base_inicio, busquedaNombreCurso, busquedaApellidoEstudiante, \
    profesor, busquedaProfesionProfesor, crearCursoURL, crearCurso, crearEstudiante, crearProfesor, eliminarCurso, \
    eliminarEstudiante, eliminarProfesor, editarCurso, editarEstudiante, editarProfesor

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', base_inicio, name="AppCoder1Base"),
    path('busqCurso/', busquedaNombreCurso, name="AppCoderBusqCurso"),
    path('curso/', curso, name="AppCoder1Curso"),
    path('curso/crear', crearCurso, name="AppCoder1CrearCurso"),
    path('curso/editar/<camada>', editarCurso, name="AppCoder1EditarCurso"),
    path('curso/eliminar/<camada>', eliminarCurso, name="AppCoder1EliminarCurso"),
    path('alumno/eliminar/<apellido>', eliminarEstudiante, name="AppCoder1EliminarEstudiante"),
    path('alumno/editar/<apellido>', editarEstudiante, name="AppCoder1EditarEstudiante"),
    path("alumno/", estudiante, name="AppCoder1Alumno"),
    path("alumno/crear", crearEstudiante, name="AppCoder1CrearAlumno"),
    path("profesor/", profesor, name="AppCoder1Profesor"),
    path("profesor/crear", crearProfesor, name="AppCoder1CrearProfesor"),
    path("busqAlumno/", busquedaApellidoEstudiante, name="AppCoder1BusqAlumno"),
    path("busqProfesion/", busquedaProfesionProfesor, name="AppCoder1BusqProfesion"),
    path('profesor/eliminar/<apellido>', eliminarProfesor, name="AppCoder1EliminarProfesor"),
    path('profesor/editar/<apellido>', editarProfesor, name="AppCoder1EditarProfesor"),
    path("guardar/<nombre>/<idc>", crearCursoURL, name="AppCoder1Guardar")
]