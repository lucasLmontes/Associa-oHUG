from django.urls import path
from aplic.views import index, turma

urlpatterns = [
    path('', index, name='index.html'),
    path('turma/', turma, name='turma.html'),
]
