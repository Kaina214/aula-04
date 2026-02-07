from django.db import models

# CHAMADO
class Chamado(models.Model):
    laboratorio = models.CharField(max_length=100)
    descricao = models.TextField()

    OPCOES_PRIORIDADE = [
        ('Baixa', 'Baixa'),
        ('Media', 'Média'),
        ('Alta', 'Alta'),
    ]
    prioridade = models.CharField(max_length=10, choices=OPCOES_PRIORIDADE, default='Media')

    data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.laboratorio} - {self.prioridade}"

# CATEGORIA
class Categoria(models.Model):
    nome = models.CharField(max_length=100)
    data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome

# EQUIPAMENTOS
class Equipamentos(models.Model):
    descricao = models.CharField(max_length=250)
    tipo = models.CharField(max_length=50)
    ocupado = models.BooleanField(default=False)

    OPCOES_CONDICAO = [
        ('Novo', 'Novo'),
        ('Usado', 'Usado'),
        ('Defeituoso', 'Defeituoso'),
    ]
    condicao = models.CharField(max_length=50, choices=OPCOES_CONDICAO, default='Novo')

    data_criacao = models.DateTimeField(auto_now_add=True)

    # Relacionar com Categoria (OPCIONAL mas PROFISSIONAL)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"{self.descricao} - {self.tipo}"


# PESSOA
class Pessoa(models.Model):
    cpf = models.CharField(max_length=11)
    nome = models.CharField(max_length=150)
    email = models.EmailField()
    telefone = models.CharField(max_length=20)

    data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome