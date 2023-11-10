from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import CreateView, UpdateView, ListView, DeleteView, TemplateView
from django.urls import reverse_lazy
from .models import Aluno,Curso,Cidade
from .forms import AlunoForm

class AlunoCriarView(CreateView):
    model = Aluno
    form_class = AlunoForm
    template_name = "aluno/form.html" 
    success_url = reverse_lazy('aluno_listar')

class AlunoEditarView(UpdateView):
    model = Aluno
    form_class = AlunoForm
    template_name = "aluno/form.html"
    success_url = reverse_lazy('aluno_listar')
    pk_url_kwarg = 'id'

class AlunoListarView(ListView):
    model = Aluno
    template_name = "aluno/alunos.html"
    context_object_name = 'alunos'

class AlunoDeleteView(DeleteView):

    model = Aluno
    template_name = reverse_lazy('aluno_listar')
    pk_url_kwarg = 'id'

    def get(self, request, *args, **kwargs):
        return self.delete(*args, **kwargs)

class IndexView(TemplateView):
    template_name = "aluno/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['total_alunos'] = Aluno.objects.count()
        context['total_cidades'] = Cidade.objects.count()
        context['total_cursos'] = Curso.objects.count()

        return context



