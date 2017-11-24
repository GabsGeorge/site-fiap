from django.shortcuts import render, redirect 
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import View, TemplateView, CreateView, UpdateView
from django.conf import settings 
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import EditaContaForm

from core.models import Curso
from core.models import Disciplina
from core.models import Aluno
from core.models import Professor



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
		"aluno":Aluno.objects.all()
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
	return render(request, "questionario.html")

#funcao para alterar conta
@login_required
def editarConta(request):
    template_name = 'editarConta.html'
    contexto = {}
    if request.method == 'POST':
        form = EditaContaForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            form = EditaContaForm(instance=request.user)
            context['success'] = True
    else:
        form = EditaContaForm(instance=request.user)
    contexto['form'] = form
    return render(request, template_name, contexto)


#funcao para alterar senha
@login_required
def editarSenha(request):
    template_name = 'editarSenha.html'
    context = {}
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            context['success'] = True
    else:
        form = PasswordChangeForm(user=request.user)
    context['form'] = form
    return render(request, template_name, context)    
