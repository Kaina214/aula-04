# ...existing code...
from django.shortcuts import render, redirect

# Nosso "banco" em memória
chamados = [
    {"lab": "Lab 01", "problema": "PC lento", "prioridade": "Média"},
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

def nova_categoria(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')

        # por enquanto só imprime ou redireciona
        print(nome)

        return redirect('listar')  # depois a gente melhora

    return render(request, 'core/novacategoria.html')

# ...existing code...