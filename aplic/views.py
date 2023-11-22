from django.shortcuts import render
from aplic.models import Publicacao, Recado, Atividade, Apoiador, Turma, Professor, Aluno

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
    turma=Turma.objects.order_by('ano').all()
    professor=Professor.objects.order_by('nome').all()
    aluno=Aluno.objects.order_by('nome').all()
    context={
        'turma': turma,
        'professor': professor,
        'aluno': aluno,
    }
    return render(request, 'turma.html', context)
