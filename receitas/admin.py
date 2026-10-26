from contato import admin
from .models import categoria, receita


@admin.register(categoria)
class CategoriaAdmin(admin.ModelAdmin):
   list_display = ('ordem', 'nome', 'slug')
   prepopulated_fields = {'slug': ('nome',)}
   ordering = ('ordem',)


@admin.register(receita)
class ReceitaAdmin(admin.ModelAdmin):
   list_display = ('titulo', 'categoria', 'tempo_preparo', 'destaque', 'criado_em')
   list_filter = ('categoria', 'destaque', 'ocasiao')
   search_fields = ('titulo', 'descricao', 'ingredientes')
   prepopulated_fields = {'slug': ('titulo',)}
