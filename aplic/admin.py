from django.contrib import admin
from aplic.models import Professor, Aluno, Turma, Acoes, Aviso, Atividade, Doacao

class ProfessorAdmin(admin.ModelAdmin):
    filter_horizontal = ('leciona',)

admin.site.register(Professor, ProfessorAdmin)

admin.site.register(Aluno)

admin.site.register(Turma)

admin.site.register(Acoes)

admin.site.register(Aviso)

admin.site.register(Atividade)

admin.site.register(Doacao)
