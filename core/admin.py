from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django import forms
# importa as classes do models
from core.models import Curso
from core.models import Aluno
from core.models import Disciplina
from core.models import Professor
from core.models import Matricula

class CursoAdmin(admin.ModelAdmin):
    list_display = ["sigla", "nome", "ativo", "slug"] # lista  uma tabela de cursos com os dados listados
    search_fields = ["nome", "slug"] # realiza busca de cursos por nome
    prepopulated_fields = {'slug': ('nome',)} # Cria url amigavel para navegador

class AlunoForm(forms.ModelForm):

    def save(self, commit=True):
        aluno = super(AlunoForm,self).save(commit=False)
        aluno.set_password("123@mudar")
        aluno.perfil = 'Aluno'
        if commit:
            aluno.save()
        return aluno

    class Meta:
        model = Aluno
        fields = ["ra", "nome", "email", "sigla_curso"]

class AlunoAlterarForm(forms.ModelForm):

    class Meta:
        model = Aluno
        fields = ["nome", "email", "sigla_curso"]


class AlunoAdmin(UserAdmin):
    add_form = AlunoForm
    form = AlunoAlterarForm
    add_fieldsets = ((None, { "fields": ("ra", "nome", "email", "sigla_curso")}),)
    fieldsets = ((None, { "fields": ("nome", "email", "sigla_curso")}),)
    list_display =["ra","nome","email","sigla_curso"]
    filter_horizontal = []
    ordering = ["ra"]
    list_filter = ["sigla_curso"]



# Adiciona a minha classe curso no painel admin do Django.
admin.site.register(Curso, CursoAdmin)
admin.site.register(Aluno, AlunoAdmin)
admin.site.register(Disciplina)
admin.site.register(Professor)
admin.site.register(Matricula)
