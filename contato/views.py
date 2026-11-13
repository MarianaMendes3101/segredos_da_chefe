from django.contrib import messages
from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import get_object_or_404, redirect, render
from .forms import ContatoForm
from .models import Contato


def criar_contato(request):
    if request.method == "POST":
        form = ContatoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Mensagem enviada com sucesso! Obrigado pelo contato.")
            return redirect("contato:criar")
        messages.error(request, "Confira os campos destacados e tente novamente.")
    else:
        form = ContatoForm()
    return render(request, "contato/contato_form.html", {"form": form})


@staff_member_required
def lista_contatos(request):
    return render(request, "contato/contato_list.html", {"contatos": Contato.objects.order_by("-data_envio")})


@staff_member_required
def editar_contato(request, pk):
    contato = get_object_or_404(Contato, pk=pk)
    if request.method == "POST":
        form = ContatoForm(request.POST, instance=contato)
        if form.is_valid():
            form.save()
            messages.success(request, "Contato atualizado com sucesso.")
            return redirect("contato:lista")
    else:
        form = ContatoForm(instance=contato)
    return render(request, "contato/contato_form.html", {"form": form, "contato": contato, "modo_edicao": True})


@staff_member_required
def excluir_contato(request, pk):
    contato = get_object_or_404(Contato, pk=pk)
    if request.method == "POST":
        contato.delete()
        messages.success(request, "Mensagem excluída com sucesso.")
        return redirect("contato:lista")
    return render(request, "contato/contato_confirm_delete.html", {"contato": contato})
