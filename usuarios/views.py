from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from .forms import CadastroForm, UsuarioAdminForm, UsuarioUpdateForm

Usuario = get_user_model()


# Verifica se o usuário é administrador
def eh_administrador(user):
    return user.is_authenticated and user.is_staff


# Cadastro público de clientes
def cadastro(request):
    if request.user.is_authenticated:
        return redirect("web:index")

    if request.method == "POST":
        form = CadastroForm(request.POST)

        if form.is_valid():
            usuario = form.save(commit=False)
            usuario.is_staff = False
            usuario.is_superuser = False
            usuario.save()

            messages.success(request, "Conta criada com sucesso!")
            return redirect("usuarios:login")
    else:
        form = CadastroForm()

    return render(request, "usuarios/cadastro.html", {"form": form})


# Área administrativa
@login_required
@user_passes_test(eh_administrador)
def painel_usuarios(request):
    return render(request, "usuarios/usuario_list.html", {
        "usuarios": Usuario.objects.all()
    })


# Lista de usuários
class UsuarioListView(LoginRequiredMixin, UserPassesTestMixin, ListView):
    model = Usuario
    template_name = "usuarios/usuario_list.html"
    context_object_name = "usuarios"

    def test_func(self):
        return self.request.user.is_staff


# Cadastro de usuário pelo administrador
class UsuarioCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Usuario
    form_class = UsuarioAdminForm
    template_name = "usuarios/usuario_form.html"
    success_url = reverse_lazy("usuarios:lista")
    extra_context = {"titulo_pagina": "Cadastrar usuário"}

    def test_func(self):
        return self.request.user.is_staff

    def form_valid(self, form):
        messages.success(self.request, "Usuário cadastrado com sucesso!")
        return super().form_valid(form)


# Editar usuário
class UsuarioUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Usuario
    form_class = UsuarioUpdateForm
    template_name = "usuarios/usuario_form.html"
    success_url = reverse_lazy("usuarios:lista")
    extra_context = {"titulo_pagina": "Editar usuário"}

    def test_func(self):
        return self.request.user.is_staff


# Excluir usuário
class UsuarioDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Usuario
    template_name = "usuarios/usuario_confirm_delete.html"
    context_object_name = "usuario"
    success_url = reverse_lazy("usuarios:lista")

    def test_func(self):
        return self.request.user.is_staff
