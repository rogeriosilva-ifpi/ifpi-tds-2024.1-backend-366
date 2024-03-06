from django.contrib import admin
from core.models import Clube
from django.utils.html import format_html


@admin.register(Clube)
class ClubeAdmin(admin.ModelAdmin):
    list_display = ['escudo_img', 'nome', 'cidade',
                    'ano_fundacao', 'tem_mundial', 'id']
    list_filter = ['tem_mundial']
    search_fields = ['nome',  'ano_fundacao']

    def escudo_img(self, clube):
        url = 'https://placehold.co/60'
        if clube.escudo:
            url = clube.escudo.url
        return format_html(f'<img src="{url}" width="60" />')
