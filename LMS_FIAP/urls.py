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
from core.views import Aluno
from core.views import Professor
#from core.views import detalhe_de_cursos
from core.views import questionario
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^index', index),
    url(r'^$', index),
	url(r'^noticia', noticia),
	url(r'^login', login, { "template_name":"login.html" },name="entrar"),
    url(r'^logout',logout,name="sair"),
    url(r'^aluno', Aluno, name="aluno"),
    url(r'^professor', Professor, name="professor"),
    url(r'^lista_cursos', Cursos),
    url(r'^Disciplina', Disciplina),
    #url(r'^(?P<slug>[\w_-]+)/$', detalhe_de_cursos),
    url(r'^questionario', questionario)
 ]

 
# verifica se o django está em modo de desenvolvimento (DEBUG), assim ele vai usar o diretório root dos arquivos para gerar uma view
if settings.DEBUG: 
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)