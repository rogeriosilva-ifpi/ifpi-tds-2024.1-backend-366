from pyexpat import model
from turtle import back
from django.db import models


class Estado(models.Model):
  nome = models.CharField(max_length=128, null=False, blank=False)
  sigla = models.CharField(max_length=2, null=False, blank=False)

  # virtual / dinamico (relateds)
  # cidades = List[Cidade]


class Cidade(models.Model):
  nome = models.CharField(max_length=200, null=False, blank=False)
  
  # relacionamento
  estado = models.ForeignKey(Estado, 
                             on_delete=models.CASCADE, 
                             related_name='cidades')
