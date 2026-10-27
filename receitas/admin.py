from django.contrib import admin
from .models import Categoria, Receita


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ("ordem", "nome", "slug")
    prepopulated_fields = {"slug": ("nome",)}
    ordering = ("ordem",)


@admin.register(Receita)
class ReceitaAdmin(admin.ModelAdmin):
    list_display = ("titulo", "categoria", "tempo_preparo", "destaque", "criado_em")
    list_filter = ("categoria", "destaque", "ocasiao")
    search_fields = ("titulo", "descricao", "ingredientes")
    prepopulated_fields = {"slug": ("titulo",)}
