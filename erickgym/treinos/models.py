from django.db import models


class Exercicio(models.Model):
    nome = models.CharField(max_length=250)
    descricao = models.CharField(max_length=250)
    idade_minima = models.PositiveIntegerField(default=12)
    ativo = models.BooleanField(default=True)
