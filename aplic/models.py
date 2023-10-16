from django.db import models

class Professor(models.Model):
    nome = models.CharField(('Nome'), max_length=100, default="Nome")
    materia = models.CharField(('Matéria'), max_length=100)
    turma = models.CharField(('Turma'), max_length=100)
    dataNasc = models.DateField(('Data de Nascimento'), blank=True, null=True, help_text=('Formato DD/MM/AAAA'))
    email = models.EmailField(('Email'), blank=True, null=True, max_length=100)

    class Meta:
        verbose_name = 'Professor'
        verbose_name_plural = 'Professores'

    def __str__(self):
        return f' {self.nome} / {self.materia} '

class Responsavel(models.Model):
    nome = models.CharField(('Nome'), max_length=100, default="Nome")
    dataNasc = models.DateField(('Data de Nascimento'), blank=True, null=True, help_text=('Formato DD/MM/AAAA'))
    email = models.EmailField(('Email'), blank=True, null=True, max_length=100)

    class Meta:
        verbose_name = 'Responsável'
        verbose_name_plural = 'Responsáveis'

    def __str__(self):
        return self.nome

class Aluno(models.Model):
    nome = models.CharField(('Nome'), max_length=100, default="Nome")
    matricula = models.IntegerField(('Matrícula'), unique=True)
    turma = models.CharField(('Turma'), max_length=100)
    dataNasc = models.DateField(('Data de Nascimento'), blank=True, null=True, help_text=('Formato DD/MM/AAAA'))
    email = models.EmailField(('Email'), blank=True, null=True, max_length=100)
    responsaveis = models.ManyToManyField(Responsavel, blank=True)

    class Meta:
        verbose_name = 'Aluno'
        verbose_name_plural = 'Alunos'

    def __str__(self):
        return f' {self.matricula} / {self.nome} '

class Publicacao(models.Model):
    titulo = models.CharField(('Título'), max_length=30, default='Título')
    descricao = models.TextField(('Descrição'), max_length=200)

    class Meta:
        verbose_name = 'Publicação'
        verbose_name_plural = 'Publicações'

    def __str__(self):
        return self.titulo
