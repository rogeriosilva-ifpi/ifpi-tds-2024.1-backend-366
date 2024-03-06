from django.db import models
from comum.models import Cidade


class Clube(models.Model):
    nome = models.CharField(max_length=120)
    cores = models.CharField(max_length=80, blank=True, null=True)
    ano_fundacao = models.PositiveIntegerField(default=0)
    tem_mundial = models.BooleanField(default=False)
    escudo = models.ImageField(upload_to='clubes', null=True)

    cidade = models.ForeignKey(
        Cidade, on_delete=models.CASCADE, related_name='clubes', null=True)

    def __str__(self):
        return self.nome
