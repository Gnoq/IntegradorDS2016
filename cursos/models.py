from django.db import models
from personas.models import Docente, Alumno
from .choices import ASISTENCIA, ESTADOS_CURSOS


class Curso(models.Model):
    nombre = models.CharField(
        max_length=200,
        verbose_name=('Nombre de Curso'))
    fecha_inicio = models.DateField(
        verbose_name=('Fecha de Inicio'))
    fecha_finalizado = models.DateField(
        verbose_name=('Fecha de Finalización'))
    docente = models.ForeignKey(Docente)
    cupo = models.IntegerField(
        verbose_name=('Cupo'))
    descripcion = models.TextField(
        verbose_name=('Descripción'))
    horario_cursado = models.TextField(
        verbose_name=('Horario de cursado'))
    estado = models.CharField(
        max_length=255,
        choices=ESTADOS_CURSOS,
        null=True)

    def __str__(self):
        return self.nombre.upper()


class Cursado(models.Model):
    fecha_inscripcion = models.DateField(
        auto_now=True,
        verbose_name=('Fecha de Inscripción'))
    curso = models.ForeignKey(Curso)
    alumno = models.ForeignKey(Alumno)

    def __str__(self):
        return "{1}  {0}   {2}".format(self.fecha_inscripcion, self.curso.nombre, self.alumno.nombre_completo)

    @staticmethod
    def get_with(query):
        queryset = Cursado.objects.filter(alumno__nroAlumno=query)
        return queryset


    @staticmethod
    def get_Alumnos(query):
        queryset = Alumno.objects.filter(cursado__curso=query)
        return queryset


class Asistencia(models.Model):
    fecha = models.DateTimeField(
        auto_now=True,
        verbose_name=('Fecha'))
    cursado = models.ForeignKey(Cursado)
    presente = models.CharField(
        max_length=255,
        choices=ASISTENCIA,
        null=True)

    def __str__(self):
        return "{0} | {1} : {2}".format(self.cursado.alumno.nombre_completo, self.cursado.curso.nombre, self.presente)

    @staticmethod
    def get_with(query):
        queryset = Asistencia.objects.filter(cursado__alumno__nroAlumno=query)
        return queryset


class Nota(models.Model):
    fecha = models.DateTimeField(
        verbose_name=('Fecha'),
        null=False,
        blank=False)
    cursado = models.ForeignKey(Cursado)
    tema_evaluacion = models.TextField(
        verbose_name=('Temas evaluados'))
    nota = models.DecimalField(
        max_digits=4,
        decimal_places=2,
        verbose_name=('Nota de la evaluación'))

    def __str__(self):
        return "{0} | {1} : {2}".format(self.cursado.alumno.nombre_completo, self.cursado.curso.nombre, self.nota)

    @staticmethod
    def get_with(query):
        queryset = Nota.objects.filter(cursado__alumno__nroAlumno=query)
        return queryset
