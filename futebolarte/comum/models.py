from django.db import models


class Pais(models.Model):
    nome = models.CharField(max_length=120, null=False, blank=False)

    class Meta:
        verbose_name_plural = 'Países'

    def __str__(self):
        return self.nome


class Estado(models.Model):
    nome = models.CharField(max_length=120, null=False, blank=False)
    sigla = models.CharField(max_length=2, null=False, blank=False)

    pais = models.ForeignKey(
        Pais, on_delete=models.CASCADE, related_name='estados')

    def __str__(self):
        return self.nome


class Cidade(models.Model):
    nome = models.CharField(max_length=120, null=False, blank=False)

    estado = models.ForeignKey(
        Estado, on_delete=models.CASCADE, related_name='cidades')

    def __str__(self):
        return f'{self.nome} - {self.estado.sigla} ({self.estado.pais.nome})'
