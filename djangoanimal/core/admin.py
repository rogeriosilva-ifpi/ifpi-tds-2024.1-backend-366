from django.contrib import admin
from core.models import Animal


@admin.register(Animal)
class AnimalAdmin(admin.ModelAdmin):
  list_display = ['nome', 'sexo', 'ano_nascimento']
  list_filter = ['sexo']
  search_fields = ['nome', 'sexo']

  
