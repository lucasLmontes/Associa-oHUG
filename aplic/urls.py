from django.urls import path
from aplic.views import index, turma, cadastro

urlpatterns = [
    path('', index, name='index.html'),
    path('turma/', turma, name='turma.html'),
    path('cadastro/', cadastro, name='cadastro.html'),
]
