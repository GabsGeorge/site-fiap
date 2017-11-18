from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
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

# Adiciona a minha classe curso no painel admin do Django.
admin.site.register(Curso, CursoAdmin)
admin.site.register(Aluno)
admin.site.register(Disciplina)
admin.site.register(Professor)
admin.site.register(Matricula)
