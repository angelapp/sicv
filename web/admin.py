from django.contrib import admin
from django import forms
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from django.contrib.admin.widgets import FilteredSelectMultiple
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import Group


from .models import *




class ProgramaEstudiantesAdminForm(forms.ModelForm):
    usuario = forms.ModelMultipleChoiceField(
        queryset = Usuario.objects.filter(groups__name='Estudiantes'),
        required=True,
        widget=FilteredSelectMultiple(
        verbose_name=_('Estudiantes'),
        is_stacked=False
        )
    )

    programa = forms.ModelMultipleChoiceField(
        queryset = Programa.objects.all(),
        required=True,
        widget=FilteredSelectMultiple(
        verbose_name=_('Programas'),
        is_stacked=False
        )
    )




class ProgramaEstudiantesAdmin(admin.ModelAdmin):
    #form = ProgramaEstudiantesAdminForm
    list_display = ['fecha_inscripcion', 'status', 'usuario', 'programa']
    raw_id_fields = ('usuario', 'programa',)




class ProgramaAdminForm(forms.ModelForm):
    cursos = forms.ModelMultipleChoiceField(
        queryset = Curso.objects.all(),
        required=True,
        widget=FilteredSelectMultiple(
        verbose_name=_('Cursos'),
        is_stacked=False
        )
    )

class ProgramaAdmin(admin.ModelAdmin):
    form = ProgramaAdminForm
    list_display = ['codigo', 'nombre', 'activo', 'duracion']
    search_fields = ('codigo', 'nombre')

class CursoAdmin(admin.ModelAdmin):
    list_display = ['codigo', 'nombre', 'num_estudiantes']





class UsuarioEstudianteFormularioCrear(UserCreationForm):

    class Meta:
        model = Usuario
        fields = ('codigo', 'first_name' , 'last_name', 'email', 'identificacion', 'telefono', 'edad', 'resultado_examen', 'pais', 'ciudad', 'genero', 'tipo_identificacion', 'pregrado_egreso', 'colegio_egreso')

    def save(self, commit=True):
        #supervisor = self.cleaned_data['supervisor']
        # Save user first 
        user = super(UsuarioEstudianteFormularioCrear, self).save(commit=True)
        user.username = self.cleaned_data['codigo']
        group, __ = Group.objects.get_or_create(name='Estudiantes')
        group.user_set.add(user)
        group.save()
        user.save()
        return user




class UsuarioEstudianteFormularioCambiar(UserChangeForm):

    class Meta:
        model = Usuario
        fields = ('first_name' , 'last_name', 'email', 'identificacion', 'telefono', 'edad', 'resultado_examen', 'pais', 'ciudad', 'genero', 'tipo_identificacion', 'pregrado_egreso', 'colegio_egreso')



class UsuarioAdmin(admin.ModelAdmin):
    list_display = ['username', 'codigo', 'first_name', 'last_name', 'group', 'is_staff', 'is_active']
    list_filter = ["is_active"]
    change_form = UsuarioEstudianteFormularioCambiar
    add_form = UsuarioEstudianteFormularioCrear
    search_fields = ('codigo', 'first_name')

    def group(self, user):
        groups = []
        for group in user.groups.all():
            groups.append(group.name)
        return ' '.join(groups)
    group.short_description = 'Grupo'


    def get_form(self, request, obj=None, **kwargs):
        
        if request.user.is_superuser:
            pass
        else:
            if not obj:
                self.form = self.add_form
            else:
                self.form = self.change_form

        return super(UsuarioAdmin, self).get_form(request, obj, **kwargs)
    
   
   
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        elif request.user.groups.filter(name='Coordinadores').exists():
            qs = Usuario.objects.filter(groups__name='Estudiantes')
            return qs
        else:
            return None



admin.site.register(Usuario, UsuarioAdmin)
admin.site.register(Pais)
admin.site.register(Ciudad)
admin.site.register(Genero)
admin.site.register(TipoIdentificacion)
admin.site.register(Facultad)
admin.site.register(Modalidad)
admin.site.register(Jornada)
admin.site.register(Curso, CursoAdmin)
admin.site.register(Programa, ProgramaAdmin)
admin.site.register(ProgramaUsuario, ProgramaEstudiantesAdmin)
admin.site.register(CursoUsuario)
admin.site.register(PregradosEgreso)
admin.site.register(ColegioEgreso)
admin.site.register(Contacto)
admin.site.register(CursoSemestre)

