from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission

class Usuario(AbstractUser):
    login = models.CharField(('Login'), max_length=100)

    groups = models.ManyToManyField(
        Group,
        related_name='custom_user_groups',
    )

    user_permissions = models.ManyToManyField(
        Permission,
        related_name='custom_user_permissions',
    )

class Perfil(models.Model):
    nome = models.CharField(('Nome'), max_length=100, default='Nome')
    dataNasc = models.DateField(('Data de Nascimento'), blank=True, null=True, help_text=('Formato DD/MM/AAAA'))
    email = models.EmailField(('Email'), blank=True, null=True, max_length=100)

    class Meta:
        abstract = True

    def __str__(self):
        return self.nome

class Turma(models.Model):
    ano = models.CharField(('Ano'), max_length=50)

    class Meta:
        verbose_name = 'Turma'
        verbose_name_plural = 'Turmas'
    
    def __str__(self):
        return self.ano

class Professor(Perfil):
    leciona = models.ManyToManyField(Turma)

    class Meta:
        verbose_name = 'Professor'
        verbose_name_plural = 'Professores'

class Aluno(Perfil):
    matricula = models.IntegerField(('Matrícula'), unique=True, default='0000000')
    turma = models.ForeignKey(Turma, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Aluno'
        verbose_name_plural = 'Alunos'

class Acoes(models.Model):
    titulo = models.CharField(('Título'), max_length=50, default='Título')
    descricao = models.TextField(('Descrição'), max_length=250)
    imagem = models.ImageField(('Imagem'), upload_to='media/', blank=True, null=True)

    class Meta:
        verbose_name = 'Ação'
        verbose_name_plural = 'Ações'

    def __str__(self):
        return self.titulo

class Aviso(models.Model):
    preview = models.CharField(('Preview'), blank=True, max_length=50)
    texto = models.TextField(('Aviso'), blank=True, max_length=500)

    class Meta:
        verbose_name = 'Aviso'
        verbose_name_plural = 'Avisos'

    def __str__(self):
        return self.preview

class Atividade(models.Model):
    titulo = models.CharField(('Atividade'), max_length=50)
    descricao = models.TextField(('Descrição'), blank=True, max_length=250)
    turma = models.ForeignKey(Turma, blank=True, null=True, on_delete=models.CASCADE)
    referLink = models.CharField(('Referência do Link'), max_length=50, default='Atividade x')
    link = models.URLField(('Link da Atividade'))

    class Meta:
        verbose_name = 'Atividade'
        verbose_name_plural = 'Atividades'

    def __str__(self):
        return self.titulo

class Doacao(models.Model):
    descricao = models.TextField(('Descrição'), max_length=500)
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE, blank=True, null=True)
    itens = models.CharField(('Itens'), max_length=500)
    linkDoacoes = models.URLField(('Link para Doações'))

    class Meta:
        verbose_name = 'Doação'
        verbose_name_plural = 'Doações'

    def __str__(self):
        return self.aluno
