from django.shortcuts import render
from aplic.models import Publicacao, Recado, Atividade, Apoiador

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
