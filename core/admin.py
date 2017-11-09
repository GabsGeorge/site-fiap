from django.contrib import admin
# importa a classe curso
from core.models import Curso
from core.models import Aluno
from core.models import Disciplina
from core.models import Professor

# Adiciona a minha classe curso no painel admin do Django.
admin.site.register(Curso)
admin.site.register(Aluno)
admin.site.register(Disciplina)
admin.site.register(Professor)

