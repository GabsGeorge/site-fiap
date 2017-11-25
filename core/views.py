from django.shortcuts import render, get_object_or_404, redirect 
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import View, TemplateView, CreateView
from django.conf import settings 
from django.contrib.auth import get_user_model

from core.models import Curso
from core.models import Disciplina
from core.models import Aluno

User = get_user_model()


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
	contexto = {
		"cursos":Curso.objects.all()
	}
	return render(request, "aluno.html", contexto)

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
	# resquest.POST
	# Tentei salvar no BD as respostas e não obtive sucesso.
	# Resposta.objects.create (
	# 	resposta1=request.POST.cleaned_data("resposta1"),
	# 	resposta2=request.POST.cleaned_data("resposta2"),
	# 	resposta3=request.POST.cleaned_data("resposta3"),
	# 	alternativa_4=request.POST.cleaned_data("alternativa_4"),
	# 	alternativa_5=request.POST.cleaned_data("alternativa_5"),
	# 	alternativa_6=request.POST.cleaned_data("alternativa_6"),
	# 	alternativa_7=request.POST.cleaned_data("alternativa_7"),
	# 	alternativa_8=request.POST.cleaned_data("alternativa_8"),
	# 	alternativa_9=request.POST.cleaned_data("alternativa_9"),
	# 	alternativa_10=request.POST.cleaned_data("alternativa_10")
	# )
	return render(request, "questionario.html")

def registro(request):
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect(settings.LOGIN_URL)
	else:
		form = UserCreationForm()
	contexto = {
		'formulario': UserCreationForm()
	}
	return render(request, 'cadastro_aluno.html', contexto)