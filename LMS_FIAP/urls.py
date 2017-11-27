"""LMS_FIAP URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth.views import login, logout
from core.views import index
from core.views import noticia
from core.views import Cursos
from core.views import Disciplina
from core.views import aluno
from core.views import professor
from core.views import coordenador
from core.views import detalhe_de_cursos
from core.views import questionario
from core.views import editarConta
from core.views import editarSenha
from core.views import redirec
from core.views import Boletim
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^index', index, name="index"),
    url(r'^$', index),
    url(r'^noticia', noticia),
    url(r'^login', login, { "template_name":"login.html" },name="entrar"),
    url(r'^logout',logout,name="sair"),
    url(r'^aluno', aluno, name="aluno"),
    url(r'^professor', professor, name="professor"),
    url(r'^coordenador', coordenador, name="coordenador"),
    url(r'^lista-de-cursos', Cursos , name="lista-de-cursos" ),
    url(r'^Disciplina', Disciplina),
    url(r'^(?P<slug>[\w_-]+)/$', detalhe_de_cursos),
    url(r'^EAD', questionario, name="EAD"),
    url(r'^editar-conta', editarConta, name="editar-conta"),
    url(r'^editar-senha', editarSenha, name="editar-senha"),
    url(r'^boletim', Boletim),
    url(r'^redirec', redirec)
    
 ]

 
# verifica se o django está em modo de desenvolvimento (DEBUG), assim ele vai usar o diretório root dos arquivos para gerar uma view
if settings.DEBUG: 
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)