from django.shortcuts import render, redirect, get_object_or_404
from .models import Chamado

def home(request):
    chamados = Chamado.objects.all()
    return render(request, 'core/home.html', {'chamados': chamados})

def listar(request):
    chamados = Chamado.objects.all()
    return render(request, 'core/listar.html', {'chamados': chamados})

def listar_chamados(request):
    chamados = Chamado.objects.all()
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
        return redirect('listar')

    return render(request, 'core/novo_chamado.html')

def fechar(request, indice):
    chamado = get_object_or_404(Chamado, pk=indice)
    chamado.delete()
    return redirect('listar')

def nova_categoria(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        Categoria.objects.create(nome=nome)
        return redirect('listar_categorias')

    return render(request, 'core/novaCategoria.html')

def listar_categorias(request):
    categorias = Categoria.objects.all()
    return render(request, 'core/listar_categorias.html', {'categorias': categorias})