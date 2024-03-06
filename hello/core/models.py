from django.db import models

# Create your models here.
class Animal(models.Model):
  nome = models.CharField(null=True, blank=True, max_length=100)

  def __str__(self):
    return self.nome
