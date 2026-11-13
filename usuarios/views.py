from django.contrib import messages
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import get_object_or_404, redirect, render
from .forms import CadastroUsuarioForm, UsuarioAdminForm
from .models import Usuario


def cadastro(request):
    if request.method == "POST":
        form = CadastroUsuarioForm(request.POST)
        if form.is_valid():
            usuario = form.save()
            messages.success(request, "Conta criada com sucesso. Você já pode entrar.")
            return redirect("usuarios:login")
    else:
        form = CadastroUsuarioForm()
    return render(request, "usuarios/cadastro.html", {"form": form})


def somente_equipe(user):
    return user.is_authenticated and user.is_staff


@user_passes_test(somente_equipe)
def lista_usuarios(request):
    return render(request, "usuarios/usuario_list.html", {"usuarios": Usuario.objects.order_by("username")})


@user_passes_test(somente_equipe)
def editar_usuario(request, pk):
    usuario = get_object_or_404(Usuario, pk=pk)
    if request.method == "POST":
        form = UsuarioAdminForm(request.POST, instance=usuario)
        if form.is_valid():
            form.save()
            messages.success(request, "Usuário atualizado com sucesso.")
            return redirect("usuarios:lista")
    else:
        form = UsuarioAdminForm(instance=usuario)
    return render(request, "usuarios/usuario_form.html", {"form": form, "titulo_pagina": "Editar usuário"})


@user_passes_test(somente_equipe)
def excluir_usuario(request, pk):
    usuario = get_object_or_404(Usuario, pk=pk)
    if usuario.pk == request.user.pk:
        messages.error(request, "Você não pode excluir a própria conta por esta tela.")
        return redirect("usuarios:lista")
    if request.method == "POST":
        usuario.delete()
        messages.success(request, "Usuário excluído com sucesso.")
        return redirect("usuarios:lista")
    return render(request, "usuarios/usuario_confirm_delete.html", {"usuario": usuario})
