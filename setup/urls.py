"""
URL configuration for setup project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from core.views import home, listar, fechar, novo_chamado
from core.views import nova_categoria
from core.views import listar_chamados, listar_categorias, editar_categoria


urlpatterns = [
     path('admin/', admin.site.urls),
    
    path('nova-categoria/', nova_categoria, name='nova-categoria'),
    path('listar-chamados/', listar_chamados, name='listar-chamados'),
    path('listar-chamados/', listar_chamados, name='listar_chamados'),
    path('listar-categorias/', listar_categorias, name='listar-categorias'),
    path('', home, name='home'),
    path('listar/', listar, name='listar'),
    path('novo-chamado/', novo_chamado, name='novo-chamado'),
    path('categorias/', listar_categorias, name='listar_categorias'),
    path('editar-categoria/<int:id>/', editar_categoria, name='editar_categoria'),
    path('fechar/<int:indice>/', fechar, name='fechar-chamado'),
]


# Note: The 'novo_chamado' view is not included in the urlpatterns.