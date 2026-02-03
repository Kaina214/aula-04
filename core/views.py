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
        lab = request.POST.get('laboratorio')
        problema = request.POST.get('problema')
        if not lab or not problema:
            return render(request, 'core/novo_chamado.html', {
                'erro': 'Preencha todos os campos.',
                'lab': lab,
                'problema': problema
            })
        chamados.append({
            "lab": lab,
            "problema": problema,
            "prioridade": "Média"
        })
        return redirect('/listar')  # ou use redirect('listar') se tiver name='listar' nas urls
    # GET
    return render(request, 'core/novo_chamado.html')

def fechar(request, indice):
    try:
        idx = int(indice)
        del chamados[idx]
    except (ValueError, IndexError):
        return render(request, 'resultado.html', {
            'mensagem': 'Índice inválido.',
            'tipo_acao': 'erro'
        })
    return render(request, 'resultado.html', {
        'mensagem': 'Chamado removido com sucesso!',
        'tipo_acao': 'removido'
    })
# ...existing code...