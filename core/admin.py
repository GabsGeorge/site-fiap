from django.contrib import admin
# importa a classe curso
from core.models import Curso 

# Adiciona a minha classe curso no painel admin do Django.
admin.site.register(Curso)