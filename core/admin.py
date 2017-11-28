from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django import forms

# importa as classes do models
from core.models import Curso
from core.models import Aluno
from core.models import Disciplina
from core.models import Professor
from core.models import Matricula
from core.models import Usuario
from core.models import Cadastro_Boletim
from core.models import Gradecurricular
from core.models import Periodo
from core.models import Periododisciplina
from core.models import Turma

class TurmaAdmin(admin.ModelAdmin):
    list_display = ["nome_disciplina", "ano_ofertado","semestre_ofertado", "id_turma","ra_professor","turno"] # lista  uma tabela de cursos com os dados listados
    search_fields = ["semestre_ofertado", "ano_ofertado"] # realiza busca de cursos por nome
    filter_horizontal = []
    ordering = ["nome_disciplina"]
    list_filter = ["nome_disciplina"]


class MatriculaAdmin(admin.ModelAdmin):
    list_display = ["ra_aluno", "nome_disciplina", "ano_ofertado","semestre_ofertado", "id_turma"] # lista  uma tabela de cursos com os dados listados
    search_fields = ["semestre_ofertado", "ano_ofertado"] # realiza busca de cursos por nome
    filter_horizontal = []
    ordering = ["nome_disciplina"]
    list_filter = ["nome_disciplina"]


class TurmaAdmin(admin.ModelAdmin):
    list_display = ["nome_disciplina", "ano_ofertado", "semestre_ofertado","ra_professor","turno", "id_turma"] # lista  uma tabela de cursos com os dados listados
    search_fields = ["nome_disciplina", "ra_professor", "turno"] # realiza busca de cursos por nome
    filter_horizontal = []
    ordering = ["nome_disciplina"]
    list_filter = ["nome_disciplina"]


class PeriododisciplinaAdmin(admin.ModelAdmin):
    list_display = ["sigla_curso", "nome_disciplina", "ano_grade", "semestre_grade", "numero_periodo"] # lista  uma tabela de cursos com os dados listados
    search_fields = ["sigla_curso", "ano_grade", "semestre_grade"] # realiza busca de cursos por nome
    filter_horizontal = []
    ordering = ["nome_disciplina"]
    list_filter = ["nome_disciplina"]


class PeriodoAdmin(admin.ModelAdmin):
    list_display = ["sigla_curso", "ano_grade", "semestre_grade", "numeroperiodo"] # lista  uma tabela de cursos com os dados listados
    search_fields = ["sigla_curso", "ano_grade", "semestre_grade"] # realiza busca de cursos por nome
    filter_horizontal = []
    ordering = ["sigla_curso"]
    list_filter = ["sigla_curso"]

class GradecurricularAdmin(admin.ModelAdmin):
    list_display = ["sigla_curso", "ano", "semestre"] # lista  uma tabela de cursos com os dados listados
    search_fields = ["sigla_curso", "ano"] # realiza busca de cursos por nome
    filter_horizontal = []
    ordering = ["sigla_curso"]
    list_filter = ["sigla_curso"]

class BoletimAdmin(admin.ModelAdmin):
    list_display = ["nome_disciplina", "regular", "ra_aluno", "curso" ]


class UsuariomAdmin(admin.ModelAdmin):
    list_display = ["nome", "ra", "email", "perfil" ]
    search_fields = ["nome", "ra", "perfil"] # realiza busca de cursos por nome
    filter_horizontal = []
    ordering = ["ra"]
    list_filter = ["perfil"]


class CursoAdmin(admin.ModelAdmin):
    list_display = ["sigla", "nome", "ativo", "slug"] # lista  uma tabela de cursos com os dados listados
    search_fields = ["nome", "slug"] # realiza busca de cursos por nome
    prepopulated_fields = {'slug': ('nome',)} # Cria url amigavel para navegador


class ProfessorForm(forms.ModelForm):

    def save(self, commit=True):
        professor = super(ProfessorForm,self).save(commit=False)
        professor.set_password("123@professor")
        professor.perfil = 'professor'
        if commit:
            professor.save()
        return professor

    class Meta:
        model = Professor
        fields = ["ra", "apelido", "nome", "email", "celular"]

class ProfessorAlterarForm(forms.ModelForm):

    class Meta:
        model = Professor
        fields = ["ra", "apelido", "nome", "email", "celular"]

class ProfessorAdmin(UserAdmin):
    add_form = ProfessorForm
    form = ProfessorAlterarForm
    add_fieldsets = ((None, { "fields": ("ra", "apelido", "nome", "email", "celular")}),)
    fieldsets = ((None, { "fields": ("nome", "email", "celular")}),)
    list_display =["ra","nome","email"]
    filter_horizontal = []
    ordering = ["ra"]
    list_filter = ["nome"]



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
admin.site.register(Turma, TurmaAdmin)
admin.site.register(Professor, ProfessorAdmin)
admin.site.register(Matricula, MatriculaAdmin)
admin.site.register(Usuario, UsuariomAdmin)
admin.site.register(Cadastro_Boletim, BoletimAdmin)
admin.site.register(Gradecurricular, GradecurricularAdmin)
admin.site.register(Periodo, PeriodoAdmin)
admin.site.register(Periododisciplina, PeriododisciplinaAdmin)
