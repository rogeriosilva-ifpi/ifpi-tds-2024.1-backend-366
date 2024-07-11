from django.db import models

class Estado(models.Model):
    nome = models.CharField(max_length=128, null=False, blank=False)
    sigla = models.CharField(max_length=2, null=False, blank=False)

    # cidades = List[Cidade]

    @property
    def quantidade_cidades(self):
        return self.cidades.count()

    def __str__(self):
        return self.nome


class Cidade(models.Model):
    nome = models.CharField(max_length=128, null=False, blank=False)

    estado = models.ForeignKey(Estado, 
                    on_delete=models.CASCADE, 
                    related_name='cidades')
    
    def __str__(self):
        return self.nome
