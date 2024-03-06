from django.db import models


class Vendedor(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome[::-1]


class Tag(models.Model):
    nome = models.CharField(max_length=32)

    produto = models.ForeignKey(
        'Produto', on_delete=models.CASCADE, related_name='tags')

    def __str__(self):
        return self.nome


class Categoria(models.Model):
    nome = models.CharField(max_length=128)

    def __str__(self):
        return self.nome


UNIDADE_CHOICES = (
    ('KG', 'Quilo'),
    ('UND', 'Unidade'),
    ('SACO', 'Saco')
)


class Produto(models.Model):
    nome = models.CharField(max_length=128)
    descricao = models.CharField(max_length=1000)
    preco = models.DecimalField(decimal_places=2, max_digits=8)
    estoque = models.IntegerField(default=0)
    unidade = models.CharField(
        choices=UNIDADE_CHOICES, default='UNIDADE', max_length=120)
    habilitado = models.BooleanField(
        default=True, help_text='Se tá disponível para venda')

    # relacionamentos
    categoria = models.ForeignKey(
        Categoria, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.nome
