from django.contrib import messages
from django.db.models import ProtectedError
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .forms import CategoriaForm, ReceitaForm
from .models import Categoria, Receita


def index(request):
    return redirect("receitas:receita_list")


class CategoriaListView(ListView):
    model = Categoria
    template_name = "receitas/categoria_list.html"
    context_object_name = "categorias"


class CategoriaCreateView(CreateView):
    model = Categoria
    form_class = CategoriaForm
    template_name = "receitas/form.html"
    success_url = reverse_lazy("receitas:categoria_list")
    extra_context = {"titulo_pagina": "Cadastrar categoria", "voltar_url": "receitas:categoria_list", "tipo_registro": "categoria"}

    def form_valid(self, form):
        messages.success(self.request, "Categoria cadastrada com sucesso.")
        return super().form_valid(form)


class CategoriaUpdateView(UpdateView):
    model = Categoria
    form_class = CategoriaForm
    template_name = "receitas/form.html"
    success_url = reverse_lazy("receitas:categoria_list")
    extra_context = {"titulo_pagina": "Editar categoria", "voltar_url": "receitas:categoria_list", "tipo_registro": "categoria"}

    def form_valid(self, form):
        messages.success(self.request, "Categoria atualizada com sucesso.")
        return super().form_valid(form)


class CategoriaDeleteView(DeleteView):
    model = Categoria
    template_name = "receitas/confirm_delete.html"
    success_url = reverse_lazy("receitas:categoria_list")
    extra_context = {"titulo_pagina": "Excluir categoria", "voltar_url": "receitas:categoria_list"}

    def form_valid(self, form):
        try:
            response = super().form_valid(form)
        except ProtectedError:
            messages.error(self.request, "Esta categoria possui receitas vinculadas. Remova ou altere essas receitas antes de excluí-la.")
            return redirect("receitas:categoria_list")
        messages.success(self.request, "Categoria excluída com sucesso.")
        return response


class ReceitaListView(ListView):
    model = Receita
    template_name = "receitas/receita_list.html"
    context_object_name = "receitas"

    def get_queryset(self):
        queryset = Receita.objects.select_related("categoria")
        termo = self.request.GET.get("s", "").strip()
        categoria = self.request.GET.get("categoria", "").strip()
        if termo:
            queryset = queryset.filter(titulo__icontains=termo)
        if categoria.isdigit():
            queryset = queryset.filter(categoria_id=int(categoria))
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categorias"] = Categoria.objects.all()
        context["termo_busca"] = self.request.GET.get("s", "")
        context["categoria_selecionada"] = self.request.GET.get("categoria", "")
        return context


class ReceitaDetailView(DetailView):
    model = Receita
    template_name = "receitas/receita_detail.html"
    context_object_name = "receita"


class ReceitaCreateView(CreateView):
    model = Receita
    form_class = ReceitaForm
    template_name = "receitas/form.html"
    success_url = reverse_lazy("receitas:receita_list")
    extra_context = {"titulo_pagina": "Cadastrar receita", "voltar_url": "receitas:receita_list", "tipo_registro": "receita"}

    def form_valid(self, form):
        messages.success(self.request, "Receita cadastrada com sucesso.")
        return super().form_valid(form)


class ReceitaUpdateView(UpdateView):
    model = Receita
    form_class = ReceitaForm
    template_name = "receitas/form.html"
    success_url = reverse_lazy("receitas:receita_list")
    extra_context = {"titulo_pagina": "Editar receita", "voltar_url": "receitas:receita_list", "tipo_registro": "receita"}

    def form_valid(self, form):
        messages.success(self.request, "Receita atualizada com sucesso.")
        return super().form_valid(form)


class ReceitaDeleteView(DeleteView):
    model = Receita
    template_name = "receitas/confirm_delete.html"
    success_url = reverse_lazy("receitas:receita_list")
    extra_context = {"titulo_pagina": "Excluir receita", "voltar_url": "receitas:receita_list"}

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, "Receita excluída com sucesso.")
        return response
