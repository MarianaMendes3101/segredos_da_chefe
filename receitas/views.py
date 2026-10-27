from django.shortcuts import get_object_or_404, render
from .models import Receita, Categoria


def index(request):
    destaques = Receita.objects.filter(destaque=True)
    return render(request, "web/index.html", {
        "destaques": destaques,
    })


def home_view(request):
    return index(request)


def receitas_view(request):
    receitas = Receita.objects.all()
    categorias = Categoria.objects.all()

    termo = request.GET.get("s") or request.GET.get("busca")
    if termo:
        receitas = receitas.filter(titulo__icontains=termo)

    categoria_slug = request.GET.get("categoria")
    if categoria_slug:
        receitas = receitas.filter(categoria__slug=categoria_slug)

    return render(request, "web/receita.html", {
        "receitas": receitas,
        "categorias": categorias,
    })


def receita(request, id):
    receita_unica = get_object_or_404(Receita, pk=id)
    return render(request, "web/receita.html", {
        "receita": receita_unica,
    })


def detalhe_receita(request, receita_id):
    receita_unica = get_object_or_404(Receita, pk=receita_id)
    return render(request, "web/receita.html", {
        "receita": receita_unica,
    })
