from django.contrib import admin
from django.urls import path
from core.views import (
    home,
    novo_chamado,
    listar_chamados,
    fechar_chamado,
    listar_categorias,
    nova_categoria,
    editar_chamados,
    excluir_categoria
)

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', home, name='home'),

    path('novo-chamado/', novo_chamado, name='novo-chamado'),
    path('listar-chamados/', listar_chamados, name='listar-chamados'),
    path('fechar/<int:id>/', fechar_chamado, name='fechar-chamado'),

    path('listar-categorias/', listar_categorias, name='listar-categorias'),
    path('nova-categoria/', nova_categoria, name='nova-categoria'),
    path('excluir-categoria/<int:id>/', excluir_categoria, name='excluir-categoria'),

    path('editar-chamado/<int:id>/', editar_chamados, name='editar-chamado'),
]
