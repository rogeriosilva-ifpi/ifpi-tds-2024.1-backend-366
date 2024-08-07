from django.db import models
from cadastro.models import (
    Aluno, Professor
)


class Exercicio(models.Model):
    nome = models.CharField(max_length=250)
    descricao = models.CharField(max_length=250)
    idade_minima = models.PositiveIntegerField(default=12)
    ativo = models.BooleanField(default=True)


class Treino(models.Model):
    aluno = models.ForeignKey(Aluno,
                              on_delete=models.CASCADE,
                              related_name='treinos',
                              null=False, blank=False)
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE,
                                  related_name='treinos',
                                  null=False, blank=False
                                  )


class ItemItem(models.Model):

    series = models.PositiveIntegerField()
    repeticoes = models.PositiveIntegerField()

    exercicio = models.ForeignKey(Exercicio,
                                  on_delete=models.CASCADE,
                                  null=False, blank=False)
    treino = models.ForeignKey(Treino,
                               on_delete=models.CASCADE,
                               related_name='itens',
                               null=False, blank=False)
