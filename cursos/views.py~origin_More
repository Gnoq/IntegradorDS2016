from django.http import HttpResponse
import datetime
from cursos.models import *
from cursos.forms import *
from personas.models import Alumno
from django.forms import formset_factory
from django.shortcuts import render


def index(request):
    return render(request, 'base.html', {})


def fecha(request):
    now = datetime.datetime.now()
    html = "<html><body>Hoy es {0}</body></html>".format(now)
    return HttpResponse(html)


def cursos(request):
     return render(request, 'cursos.html', {'cursos': Curso.objects.all()})


def busqueda(request):
    if request.method == 'POST':
        form = SearchFormLegajoAlumno(request.POST)
        if form.is_valid():
            nroAlumno = form.cleaned_data['query']
            alumno = Alumno.get_with(nroAlumno)
            cursados = Cursado.get_with(nroAlumno)
            asistencias = Asistencia.get_with(nroAlumno)
            notas = Nota.get_with(nroAlumno)
            return render(request,
                          'resultados.html',
                          {'nroAlumno': nroAlumno,
                           'alumno': alumno,
                           'cursados': cursados,
                           'asistencias': asistencias,
                           'notas': notas})
    else:
        form = SearchFormLegajoAlumno()

    return render(request, 'busqueda.html', {'form': form})


def busquedaCurso(request):
    if request.method == 'POST':
        form = SearchCursoForm(request.POST)
        if form.is_valid():
            curso = form.cleaned_data['curso']
            alumnosRelacionados = Cursado.get_Alumnos(curso)
            return render(request,
                          'resultadosAsistencia.html',
                          {'curso': curso,
                           'alumnosRelacionados': alumnosRelacionados})
    else:
        form = SearchCursoForm()

    return render(request, 'busquedaCursoAsistencias.html', {'form': form})


def guardarAsistencia(request):
    if request.method == 'POST':
        asistencias = request.POST.getlist('asistencia')
        import pdb;
        pdb.set_trace()
        return render(request,'base.html')
