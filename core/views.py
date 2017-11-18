from django.shortcuts import render, get_object_or_404 
from core.models import Curso
from core.models import Disciplina

#Aqui estão as paginas views do template


def index(request):
	return render(request, "index.html")


def noticia(request):
	return render(request, "noticias.html")


def login(request):
	return render(request, "login.html")


def Cursos(request):
	contexto = {
		"cursos":Curso.objects.all()
	}
	return render(request,"lista_cursos.html", contexto)

def detalhe_de_cursos (request, slug):
    context = {
        'curso': get_object_or_404(Curso, slug=slug) #verifica se a url existe, caso nao exista ele retorna erro 404
    }
    template_name = 'detalhe_de_cursos.html'
    return render(request, template_name, context)


def Disciplina(request):
	contexto = {
		"disciplinas":Disciplina.objects.all()
	}

	return render(request, "disciplinas.html")

def questionario(request):
	return render(request, "questionario.html")