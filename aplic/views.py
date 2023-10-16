from django.shortcuts import render
from aplic.models import Publicacao

def index(request):
    publicacao=Publicacao.objects.all()
    context={
        'publicacao': publicacao,
    }
    return render(request, 'index.html', context)
