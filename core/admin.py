from django.contrib import admin
    
from .models import Chamado, Categoria, Equipamento, Pessoa
# Register your models here.

# isso é para registrar os modelos no admin do django, para que possamos criar, editar e excluir os chamados, categorias, equipamentos e pessoas através do painel de administração do django.
admin.site.register(Chamado)
admin.site.register(Categoria)
admin.site.register(Equipamento)
admin.site.register(Pessoa)