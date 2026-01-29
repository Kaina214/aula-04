from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'home.html')

# Nossa lista global (Banco de Dados em memória)
chamados = [
    {"lab": "Lab 01", "problema": "PC lento", "prioridade": "Média"},
]

def listar(request):
    # Lógica para listar os chamados em HTML
    return render(request, 'listar.html', {'chamados': chamados})

def criar(request, lab, problema, prioridade):
    # Criando o dicionário e adicionando à lista
    novo = {
        "lab": lab,
        "problema": problema,
        "prioridade": prioridade
    }
    chamados.append(novo)
    
    return render(request, 'resultado.html', {
        'mensagem': f'Chamado para o {lab} criado com sucesso!',
        'tipo_acao': 'criado'
    })

def fechar(request, indice):
    del chamados[indice]
    
    return render(request, 'resultado.html', {
        'mensagem': 'Chamado removido com sucesso!',
        'tipo_acao': 'removido'
    })