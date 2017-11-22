from django.shortcuts import render, get_object_or_404 
from django.contrib.auth.decorators import login_required, user_passes_test
from core.models import Curso
from core.models import Disciplina
from core.models import Aluno

#Aqui estão as paginas views do template


def index(request):
	return render(request, "index.html")


def noticia(request):
	return render(request, "noticias.html")

def checa_aluno(usuario):
	return usuario.perfil == "Aluno"

def checa_professor(usuario):
	return usuario.perfil == "professor"

@login_required(login_url="entrar")
@user_passes_test(checa_aluno)
def aluno(request):
	return render(request, "aluno.html")

@login_required(login_url="entrar")
@user_passes_test(checa_professor)
def professor(request):
	return render(request, "professor.html")




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