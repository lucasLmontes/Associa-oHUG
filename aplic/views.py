from django.shortcuts import render
from aplic.models import Publicacao, Recado, Atividade, Apoiador, Professor, Aluno

def index(request):
    publicacao=Publicacao.objects.all()
    recado=Recado.objects.all()
    atividade=Atividade.objects.all()
    apoiador=Apoiador.objects.all()
    context={
        'publicacao': publicacao,
        'recado': recado,
        'atividade': atividade,
        'apoiador': apoiador,
    }
    return render(request, 'index.html', context)

def turma(request):
    professor=Professor.objects.all()
    aluno=Aluno.objects.all()
    context={
        'professor': professor,
        'aluno': aluno,
    }
    return render(request, 'turma.html', context)
