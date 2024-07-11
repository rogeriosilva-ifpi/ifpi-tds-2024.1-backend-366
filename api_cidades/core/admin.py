from django.contrib import admin
from core.models import Estado, Cidade


@admin.register(Estado)
class EstadoAdmin(admin.ModelAdmin):
    list_display = ['sigla', 'nome', 'quantidade_cidades']

@admin.register(Cidade)
class CidadeAdmin(admin.ModelAdmin):
    search_fields = ['nome']
