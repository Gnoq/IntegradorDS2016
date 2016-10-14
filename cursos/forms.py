from django import forms
from personas.models import Alumno
from cursos.models import Cursado, Curso, Asistencia


class SearchFormLegajoAlumno(forms.Form):
    query = forms.CharField(label='Búsqueda de alumno por Legajo', max_length=10, required=False)


class SearchCursoForm(forms.Form):
    curso = forms.ModelChoiceField(queryset=Curso.objects.all(), required=True)

    class Meta:
        model = Curso
        fields = "__all__"


class AsistenciaForm(forms.ModelForm):
    class Meta:
        model = Asistencia
        fields = ('presente','cursado')