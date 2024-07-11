from django.db import models
from django.contrib.auth.models import User


class Professor(models.Model):
    SEXO_CHOICES = (
        ('M', 'Masculino'),
        ('F', 'Feminimo'),
    )

    cpf = models.CharField(max_length=14, null=False, blank=False)
    nome = models.CharField(max_length=200, null=False, blank=False)
    telefone = models.CharField(max_length=14, null=False, blank=False)
    sexo = models.CharField(max_length=1, choices=SEXO_CHOICES)

    usuario = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        null=True,
        default=None
    )


class Aluno(models.Model):
    SEXO_CHOICES = (
        ('M', 'Masculino'),
        ('F', 'Feminimo'),
    )

    cpf = models.CharField(max_length=14, null=False, blank=False)
    nome = models.CharField(max_length=200, null=False, blank=False)
    telefone = models.CharField(max_length=14, null=False, blank=False)
    sexo = models.CharField(max_length=1, choices=SEXO_CHOICES)
    data_nascimento = models.DateField()
    foto = models.ImageField(upload_to='alunos', null=True, blank=True)

    usuario = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        null=True,
        default=None
    )
