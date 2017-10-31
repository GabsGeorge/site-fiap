from django.shortcuts import render
from core.models import Curso

def paginaPrincipal(requisicao):

	contexto = {
	
	"cursos":Curso.objects.all(),

	"faculdade":"Fit - faculdade impacta de tecnologia",
	"Pagina":"HomePage"
	
	}
	return render(requisicao, "index.html",contexto)


def noticia(request):
	return render(request, "noticias.html")


def login(request):
	return render(request, "login.html")