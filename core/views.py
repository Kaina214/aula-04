# ...existing code...
from django.shortcuts import render, redirect
from .models import Chamado
# Nosso "banco" em memória
from .models import Categoria
chamados = [
   {id: 1, "lab": "Lab 1", "problema": "Computador não liga", "prioridade": "Alta"},
   {"id": 2, "lab": "Lab 2", "problema": "Internet lenta", "prioridade": "Média"},
   {"id": 3, "lab": "Lab 3", "problema": "Impressora sem papel", "prioridade": "Baixa"},
]

def home(request):
    return render(request, 'core/home.html', {'chamados': chamados})

def listar(request):
    return render(request, 'core/listar.html', {'chamados': chamados})

def novo_chamado(request):
    if request.method == 'POST':
        lab = request.POST.get('lab')
        problema = request.POST.get('problema')
        prioridade = request.POST.get('prioridade')

        Chamado.objects.create(
            lab=lab,
            problema=problema,
            prioridade=prioridade
        )
        # por enquanto só redireciona
        return redirect('listar')

    return render(request, 'core/novo_chamado.html')
    chamados.append({
            "lab": lab,
            "problema": problema,
            "prioridade": prioridade
        })
    return redirect('/listar')  # ou use redirect('listar') se tiver name='listar' nas urls
    # GET
    return render(request, 'core/novo_chamado.html')

def fechar(request, indice):
    # Aqui você vai remover o chamado ou fazer o que quiser
    # Por enquanto vamos só redirecionar para listar
    return redirect('listar')

from django.shortcuts import render, redirect
from .models import Categoria

def nova_categoria(request):
    if request.method == "POST":
        nome = request.POST.get("nome")

        Categoria.objects.create(nome=nome)

        return redirect("listar_categorias")

    return render(request, "core/nova_categoria.html")


def listar_chamados(request):
    chamados = Chamado.objects.all()
    return render(request, "core/listar_chamados.html", {"chamados": chamados})

def listar_categorias(request):
   return redirect(request, 'core/listar_categorias.html')  # Placeholder para futura implementação

def nova_categoria(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        Categoria.objects.create(nome=nome)
    return redirect('nova-categoria')  # Placeholder para futura implementação