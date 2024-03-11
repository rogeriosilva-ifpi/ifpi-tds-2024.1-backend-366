from django.db import models

class Exercicio(models.Model):
  nome = models.CharField(max_length=250)
  ativacao_muscular = models.CharField(max_length=250)

  
