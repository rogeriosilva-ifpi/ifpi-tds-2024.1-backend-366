from django.contrib import admin
<<<<<<< HEAD
from core.models import Estado
=======
from core.models import Estado, Cidade
>>>>>>> 6be5c1bc3f4c4c87de31d30b744723fedcabb4a9


@admin.register(Estado)
class EstadoAdmin(admin.ModelAdmin):
<<<<<<< HEAD
  list_display = ['nome', 'sigla']
=======
    list_display = ['sigla', 'nome', 'quantidade_cidades']

@admin.register(Cidade)
class CidadeAdmin(admin.ModelAdmin):
    search_fields = ['nome']
>>>>>>> 6be5c1bc3f4c4c87de31d30b744723fedcabb4a9
