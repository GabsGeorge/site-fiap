from django.shortcuts import render, redirect , HttpResponseRedirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.views.generic import View, TemplateView, CreateView, UpdateView
from django.conf import settings 
from django.contrib.auth.mixins import LoginRequiredMixin
from datetime import datetime
from .forms import EditaContaAlunoForm

from core.models import Curso
from core.models import Disciplina
from core.models import Aluno
from core.models import Professor
from core.models import Matricula

#Aqui estão as paginas views do template


def index(request):

	return render(request, "index.html")

def noticia(request):
	return render(request, "noticias.html")

def checa_aluno(usuario):
	return usuario.perfil == "Aluno"

def checa_professor(usuario):
	return usuario.perfil == "professor"

def checa_coordenador(usuario):
    return usuario.perfil == "Coordenador"    

def redirec(request):
    return render(request,"redirec.html")

@login_required(login_url="entrar")
@user_passes_test(checa_aluno)
def aluno(request):
	return render(request, "aluno.html")

@login_required(login_url="entrar")
@user_passes_test(checa_professor)
def professor(request):
	return render(request, "professor.html")

@login_required(login_url="entrar")
@user_passes_test(checa_coordenador)
def coordenador(request):
    return render(request, "coordenador.html")    

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


#import do modulo datetime para os (minutos/horas/dias), e  HttpResponseRedirect para redirecionar a pagina.
#codigo abaixo separado para DIA
'''
if dia >= 29:
   return HttpResponseRedirect('/redirec.html/')  
'''

#codigo principal para os minutos 

def questionario(request):
	horaa=datetime.now()
	hora=horaa.hour
	minuto=horaa.minute
	dia=horaa.day
	fulltime=hora,":",minuto
	if fulltime >= (999,':',999):
		return HttpResponseRedirect('/redirec.html') 
	else:
		return render(request, "questionario.html")


#funcao para alterar conta
@login_required
def editarConta(request):
    template_name = 'editarConta.html'
    contexto = {}
    if request.method == 'POST':
        form = EditaContaAlunoForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            form = EditaContaAlunoForm(instance=request.user)
            contexto['success'] = True
    else:
        form = EditaContaAlunoForm(instance=request.user)
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


def Boletim(request):
    contexto = {
        'boletim': Cadastro_Boletim.objects.all()        
    }
    return render(request,"boletim.html", contexto)
