
from django.db import models
from datetime import date

class Persona(models.Model):
    apellido = models.CharField(
        max_length=255,
        verbose_name=('Apellido'))
    nombre = models.CharField(
        max_length=255,
        verbose_name=('Nombre'))
    documento = models.CharField(
        max_length=11,
        verbose_name=('Número de documento'),
        unique=True)
    fecha_nacimiento = models.DateField(
        verbose_name=('Fecha de Nacimiento'))

    @property
    def nombre_completo(self):
        return "{0}, {1}".format(
            self.apellido.upper(),
            self.nombre)

    @property
    def edad(self):
        delta = (date.today() - self.fecha_nacimiento)
        return int((delta.days / (365.2425)))

    @property
    def dni(self):
        return "{0} {1}".format(
            self.tipo_documento,
            self.documento)

    def __str__(self):
        return self.nombre_completo

    class Meta:
        ordering = ['apellido', 'nombre']
        verbose_name = ('Persona')
        verbose_name_plural = ('Personas')


class Alumno(Persona):
    nroAlumno = models.CharField(
        max_length=6,
        verbose_name=('Legajo'),
        unique=True,
    )

class Docente(Persona):
    nroDocente = models.CharField(
        max_length=6,
        verbose_name=('Legajo'),
        unique=True,
    )