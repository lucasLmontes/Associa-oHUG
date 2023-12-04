from django.shortcuts import render, redirect, get_object_or_404
from aplic.models import Membroshug, Acoes, Aviso, Doacao, Atividade, Turma, Aluno
from aplic.forms import CadastroForm, LoginForm
from django.contrib.auth import login, authenticate

def index(request):
    acao=Acoes.objects.all()
    aviso=Aviso.objects.all()
    doacao=Doacao.objects.all().order_by('-data')
    context={
        'acoes': acao,
        'avisos': aviso,
        'doacoes': doacao,
    }
    return render(request, 'index.html', context)

def membros_hug(request):
    lista_membro=Membroshug.objects.order_by('curso').all()
    return render(request, 'membros-hug.html', {'lista_membros': lista_membro})

def turma(request):
    turma=Turma.objects.order_by('ano').all()
    aluno=Aluno.objects.order_by('turma').all()
    atividade=Atividade.objects.order_by('turma').all()
    context={
        'turmas': turma,
        'alunos': aluno,
        'atividades': atividade,
    }
    return render(request, 'turma.html', context)

def contato(request):
    return render(request, 'contato.html')

def sobre_escola(request):
    return render(request, 'sobre-escola.html')

def doacao_detail_view(request, pk):
    doacao = get_object_or_404(Doacao, pk=pk)
    return render(request, 'doacao_detail.html', {'doacao': doacao})

def cadastro(request):
    if request.method == 'POST':
        form = CadastroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = CadastroForm()
    return render(request, 'cadastro.html', {'form': form})

def login_usuario(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect('index')
    else:
        form =LoginForm()
    return render(request, 'login.html', {'form': form})
