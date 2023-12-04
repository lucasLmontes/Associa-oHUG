from django.urls import path
from aplic import views

urlpatterns = [
    path('', views.index, name='index'),
    path('turma/', views.turma, name='turma'),
    path('membros/hug/', views.membros_hug, name='membros-hug'),
    path('contato/', views.contato, name='contato'),
    path('sobre/escola', views.sobre_escola, name='sobre-escola'),
    path('doacao/<int:pk>/', views.doacao_detail_view, name='doacao_detail'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('login/', views.login_usuario, name='login'),
]
