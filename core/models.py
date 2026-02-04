from django.db import models

class Chamado(models.Model):
    lab = models.CharField(max_length=100)
    problema = models.CharField(max_length=200)
    prioridade = models.CharField(max_length=20)

    def __str__(self):
        return self.problema
from django.db import models

class Categoria(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome
