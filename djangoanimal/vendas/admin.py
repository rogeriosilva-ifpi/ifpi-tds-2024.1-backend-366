from django.contrib import admin
from vendas.models import Produto, Categoria, Tag, Vendedor


class TagInline(admin.TabularInline):
    model = Tag
    extra = 0


@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ['nome', 'categoria', 'unidade', 'preco', 'habilitado']
    inlines = [TagInline]


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ['nome']


@admin.register(Vendedor)
class VendedorAdmin(admin.ModelAdmin):
    list_display = ['nome', 'id']
