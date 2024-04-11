from django.contrib import admin
from escola.models import Alunos, Cursos


class AlunosAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'rg', 'cpf', 'data_de_nascimento')
    list_display_links = ('id',)
    search_fields: ('id',)
    list_per_page = 20

admin.site.register(Alunos, AlunosAdmin)


class CursosAdmin(admin.ModelAdmin):
    list_display = ('id', 'codigo_curso', 'descricao', 'nivel_do_curso',)
    list_display_links = ('codigo_curso', 'id',)
    search_fields = ('codigo_curso',)

admin.site.register(Cursos, CursosAdmin)