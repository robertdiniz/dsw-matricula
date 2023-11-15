"""
URL configuration for main project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from aluno.views import AlunoCriarView, AlunoEditarView, AlunoDeleteView, AlunoListarView, IndexView
from curso.views import curso_listar, curso_criar, curso_remover, curso_editar
from cidade.views import cidade_criar, cidade_editar, cidade_listar, cidade_remover

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view() , name='index'),
    path('aluno/',  AlunoCriarView.as_view() , name='aluno_criar'),
    path('aluno/editar/<int:id>/', AlunoEditarView.as_view(), name='aluno_editar'),
    path('aluno/remover/<int:id>/', AlunoDeleteView.as_view(), name='aluno_remover'),
    path('aluno/listar', AlunoListarView.as_view() ,name='aluno_listar'),
    
    path('curso/',  curso_criar , name='curso_criar'),
    path('curso/listar',  curso_listar , name='curso_listar'),
    path('curso/editar/<int:id>',  curso_editar , name='curso_editar'),
    path('curso/remover/<int:id>',  curso_remover , name='curso_remover'),

    path('cidade/',  cidade_criar , name='cidade_criar'),
    path('cidade/listar',  cidade_listar , name='cidade_listar'),
    path('cidade/editar/<int:id>',  cidade_editar , name='cidade_editar'),
    path('cidade/remover/<int:id>',  cidade_remover , name='cidade_remover'),
]



