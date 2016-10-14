from django.contrib import admin
from cursos.models import (
    Cursado,
    Curso,
    Asistencia,
    Nota)

#admin.site.register(Curso)
#admin.site.register(Cursado)
#admin.site.register(Asistencia)
#admin.site.register(Nota)


@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    actions_on_bottom = True
    fieldsets = (
        (None, {
            'fields': (
                'nombre',
                'fecha_inicio',
                'fecha_finalizado',
                'docente',
                'cupo',
                'descripcion',
                'horario_cursado',)
        }),
    )
    list_display = (
        'nombre',
        'fecha_inicio',
        'fecha_finalizado',
        'docente',
        'cupo',
        'descripcion',
        'horario_cursado',)
    search_fields = (
        'nombre',
        'descripcion',
        'docente',)
    list_filter = (
        'nombre',
        'docente',
        'fecha_inicio',)
    date_hierarchy = 'fecha_inicio'


@admin.register(Cursado)
class CursadoAdmin(admin.ModelAdmin):
    actions_on_bottom = True
    list_display = (
        'alumno',
        'curso')
    search_fields = (
        'alumno__nombre',
        'alumno__apellido'
        'curso__nombre'
    )
    date_hierarchy = 'fecha_inscripcion'


@admin.register(Asistencia)
class AsistenciaAdmin(admin.ModelAdmin):
    actions_on_bottom = True
    fieldsets = (
        (None, {
            'fields': (
                'cursado',
                'presente',)
        }),
    )
    list_display = (
        'cursado',
        'presente',
        'fecha')
    search_fields = (
        'cursado__curso__nombre',
        'cursado__alumno__nombre',
        'cursado__alumno__apellido')


@admin.register(Nota)
class NotaAdmin(admin.ModelAdmin):
    actions_on_bottom = True
    fieldsets = (
        (None, {
            'fields': (
                'fecha',
                'cursado',
                'tema_evaluacion',
                'nota',)
        }),
    )
    list_display = (
        'cursado',
        'nota',)
    search_fields = (
        'cursado__curso__nombre',
        'cursado__alumno__nombre',
        'cursado__alumno__apellido',
        'nota',)
