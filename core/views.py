from django.shortcuts import render
from core.models import Curso

#Aqui estão as paginas views do template

def index(requisicao):

	contexto = {
		"cursos": Curso.objects.all(),
	}

	return render(requisicao, "index.html",contexto)


def noticia(request):
	return render(request, "noticias.html")


def login(request):
	return render(request, "login.html")



def testes(request):
	contexto = {
	
	"cursos":Curso.objects.all(),

	"faculdade":"Fit - faculdade impacta de tecnologia",
	"Pagina":"HomePage"
	
	}
	return render(request, "testes.html",contexto)

def lista_cursos(request):
	contexto = {
	
	"cursos":Curso.objects.all()
	
	}
	return render(request, "lista_cursos.html",contexto)