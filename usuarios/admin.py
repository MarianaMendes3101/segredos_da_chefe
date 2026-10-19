from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Usuario


@admin.register(Usuario)
class UsuarioAdmin(UserAdmin):
   fieldsets = UserAdmin.fieldsets + (
       ('Informações Adicionais', {'fields': ('sexo', 'data_nascimento')}),
   )
   list_display = ('username', 'email', 'first_name', 'last_name', 'sexo', 'is_staff')
