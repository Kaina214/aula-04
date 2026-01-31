from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'home.html')

# Nossa lista global (Banco de Dados em memória)
chamados = [
    {"lab": "Lab 01", "problema": "PC lento", "prioridade": "Média"},
]

def home(request):

    # Lógica para listar os chamados em HTML
    return render(request, 'core/home.html', )

    def novo_chamado(request):
        return render(request, 'core/novo_chamado.html')
        if (request.method == 'POST'):
            lab = request.POST.get('laboratorio')
            problema = request.POST.get('problema')
            print("chegou um post")
            print(f"Laboratório: {lab},Descrição: {problema}")
            
            chamados.append({
                "lab": lab,
                "problema": problema,
                "prioridade": "Média"  # Prioridade fixa por enquanto
            })
            return redirect('/listar')

            if request.method == 'GET':
                print
                return render(request, 'core/novo_chamado.html')








    # return HttpResponse(render(request, 'listar.html', {'chamados': chamados}))
    # def home_old(request):
        # return HttpResponse("Bem-vindo ao sistema de chamados!")
# def criar(request, lab, problema, prioridade):
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
def listar(request):
    return render(request, 'core/listar.html', {'chamados': chamados})