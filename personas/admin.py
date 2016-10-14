from django.contrib import admin
from personas.models import (
    Persona,
    Alumno,
    Docente)

@admin.register(Persona)
class PersonaAdmin(admin.ModelAdmin):
    actions_on_bottom = True
    fieldsets = (
        (None, {
            'fields': (
                'apellido',
                'nombre',
                'documento',
                'fecha_nacimiento',)
        }),
    )
    list_display = (
        'apellido',
        'nombre',
        'documento',
        'fecha_nacimiento',)
    search_fields = (
        'apellido',
        'nombre',
        'documento',)
    list_filter = (
        'apellido',
        'fecha_nacimiento',)
    date_hierarchy = 'fecha_nacimiento'


@admin.register(Alumno)
class AlumnoAdmin(admin.ModelAdmin):
    actions_on_bottom = True
    fieldsets = (
        (None, {
            'fields': (
                'apellido',
                'nombre',
                'documento',
                'fecha_nacimiento',
                'nroAlumno',)
        }),
    )
    list_display = (
        'apellido',
        'nombre',
        'edad',
        'documento',
        'fecha_nacimiento',
        'nroAlumno',)
    search_fields = (
        'apellido',
        'nombre',
        'documento',
        'nroAlumno')
    list_filter = (
        'apellido',
        'fecha_nacimiento',
        'nroAlumno',)
    date_hierarchy = 'fecha_nacimiento'


@admin.register(Docente)
class DocenteAdmin(admin.ModelAdmin):
    actions_on_bottom = True
    fieldsets = (
        (None, {
            'fields': (
                'apellido',
                'nombre',
                'documento',
                'fecha_nacimiento',
                'nroDocente',)
        }),
    )
    list_display = (
        'apellido',
        'nombre',
        'documento',
        'fecha_nacimiento',
        'nroDocente',)
    search_fields = (
        'apellido',
        'nombre',
        'documento',
        'nroAlumno')
    list_filter = (
        'apellido',
        'fecha_nacimiento',
        'nroDocente',)
    date_hierarchy = 'fecha_nacimiento'
