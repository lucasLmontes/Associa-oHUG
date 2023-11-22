from django.db import models

class Pessoa(models.Model):
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

class Professor(Pessoa):
    leciona = models.ManyToManyField(Turma)

    class Meta:
        verbose_name = 'Professor'
        verbose_name_plural = 'Professores'

class Aluno(Pessoa):
    matricula = models.IntegerField(('Matrícula'), unique=True, default='0000000')
    turma = models.ForeignKey(Turma, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Aluno'
        verbose_name_plural = 'Alunos'

class Publicacao(models.Model):
    titulo = models.CharField(('Título'), max_length=30, default='Título')
    descricao = models.TextField(('Descrição'), max_length=200)
    imagem = models.ImageField(('Imagem'), upload_to='media/', blank=True, null=True)

    class Meta:
        verbose_name = 'Publicação'
        verbose_name_plural = 'Publicações'

    def __str__(self):
        return self.titulo

class Recado(models.Model):
    resumo = models.CharField(('Resumo'), blank=True, max_length=30)
    texto = models.TextField(('Recado'), blank=True, max_length=200)

    class Meta:
        verbose_name = 'Recado'
        verbose_name_plural = 'Recados'

    def __str__(self):
        return self.resumo

class Atividade(models.Model):
    titulo = models.CharField(('Atividade'), max_length=100)
    descricao = models.TextField(('Descrição'), blank=True, max_length=200)
    link = models.URLField(('Link da Atividade'))

    class Meta:
        verbose_name = 'Atividade'
        verbose_name_plural = 'Atividades'

    def __str__(self):
        return self.titulo

class Apoiador(models.Model):
    marca = models.CharField(('Marca'), max_length=100)
    contato = models.CharField(('Contato'), max_length=20, unique=True, help_text='Formato (00) 0000-0000')
    email = models.EmailField(('Email'), blank=True, null=True, max_length=100)

    class Meta:
        verbose_name = 'Apoio'
        verbose_name_plural = 'Apoios'

    def __str__(self):
        return f' {self.marca} / {self.contato} '
