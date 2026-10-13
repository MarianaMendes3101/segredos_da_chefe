from django.contrib import admin
from .models import Contato


@admin.register(Contato)
class ContatoAdmin(admin.ModelAdmin):
   list_display = ('nome', 'email', 'data_envio')
   search_fields = ('nome', 'email', 'mensagem')
   readonly_fields = ('data_envio',)