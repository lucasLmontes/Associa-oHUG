from django.shortcuts import render, redirect
from aplic.models import Acoes, Aviso, Atividade, Turma, Professor, Aluno
from aplic.forms import UsuarioForm
from django.contrib.auth import login

def index(request):
    acao=Acoes.objects.all()
    aviso=Aviso.objects.all()
    context={
        'acoes': acao,
        'avisos': aviso,
    }
    return render(request, 'index.html', context)

def turma(request):
    turma=Turma.objects.order_by('ano').all()
    professor=Professor.objects.order_by('leciona').all()
    aluno=Aluno.objects.order_by('turma').all()
    atividade=Atividade.objects.order_by('turma').all()
    context={
        'turmas': turma,
        'professores': professor,
        'alunos': aluno,
        'atividades': atividade,
    }
    return render(request, 'turma.html', context)

def cadastro(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('complementar.html')
    else:
        form = UsuarioForm()

    return render(request, 'cadastro.html', {'form': form})
