from django.shortcuts import render, HttpResponse, get_object_or_404, redirect
from aluno.models import Curso
from .forms import CursoForm

def curso_criar(request):

    if request.method == 'POST':
        form = CursoForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('curso_listar')
    else:
        form = CursoForm()

        return render(request, 'curso/form.html', {'form': form})

    return HttpResponse("Criando aluno!")

def curso_listar(request):

    cursos = Curso.objects.all()

    context = {
        "cursos": cursos
    }

    return render(request, 'curso/cursos.html', context)

def curso_editar(request, id):

    curso = get_object_or_404(Curso, id=id)

    if request.method == 'POST':
        form = CursoForm(request.POST, instance=curso)

        if form.is_valid():
            form.save()
            return redirect('curso_listar')
    else:
        form = CursoForm(instance=curso)

        return render(request, 'curso/form.html', {'form': form})
    
def curso_remover(request, id):

    curso = Curso.objects.get(id=id)
    curso.delete()

    return redirect('curso_listar')