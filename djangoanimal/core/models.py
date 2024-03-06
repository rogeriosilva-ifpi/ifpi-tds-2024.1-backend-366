from django.db import models

SEXO_CHOICES = (
    ('M', 'Macho'),
    ('F', 'Fêmea'),
)


class Animal(models.Model):
    nome = models.CharField(max_length=120, null=False, blank=False)
    ano_nascimento = models.PositiveIntegerField(default=1970)
    sexo = models.CharField(choices=SEXO_CHOICES, max_length=32)

    class Meta:
        verbose_name = 'Animal'
        verbose_name_plural = 'Animais'

    def __str__(self):
        return f'Animal: {self.nome}'
