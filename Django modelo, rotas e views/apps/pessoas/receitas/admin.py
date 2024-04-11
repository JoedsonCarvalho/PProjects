from django.contrib import admin
from .models import Receita

class ListandoREceitas(admin.ModelAdmin):
    list_display = ('id', 'nome_receita', 'categoria', 'publicada')
    list_display_links = ('id', 'nome_receita')
    search_fields = ('id', 'nome_receita', )
    list_filter=('categoria', 'publicada',)
    list_editable = ('publicada',)
    list_per_page = 9

admin.site.register(Receita, ListandoREceitas)


