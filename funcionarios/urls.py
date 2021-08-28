from django import VERSION
from django.urls import path
from . import views

app_name='funcionario'

urlpatterns=[
    path('todos/',views.listar_funcionarios,name='listar_funcionarios'),
    path('cadastrar/',views.cadastrar_funcionario,name='cadastrar_funcionario'),
    path('detalhes/<int:id>/',views.detalhes_funcionario,name='detalhes_funcionario'),
    path('excluir/<int:id>/',views.excluir_funcionario,name='excluir_funcionario'),
    path('editar/<int:id>/',views.editar_funcionario,name='editar_funcionario')
]