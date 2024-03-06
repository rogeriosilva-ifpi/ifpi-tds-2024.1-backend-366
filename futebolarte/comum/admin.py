from django.contrib import admin
from comum.models import Pais, Estado, Cidade


@admin.register(Pais)
class PaisAdmin(admin.ModelAdmin):
    list_display = ['nome']


class CidadeInline(admin.TabularInline):
    model = Cidade
    extra = 0


@admin.register(Estado)
class EstadoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'sigla', 'qtd_cidades')

    inlines = [CidadeInline]

    def qtd_cidades(self, estado):
        return estado.cidades.count()
