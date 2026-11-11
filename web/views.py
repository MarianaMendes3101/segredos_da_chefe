
from django.shortcuts import render
from receitas.models import Categoria, Receita
from usuarios.models import Usuario


def index(request):
    destaques = Receita.objects.filter(destaque=True).select_related("categoria")[:6]
    recentes = Receita.objects.select_related("categoria").all()[:6]

    return render(request, "web/index.html", {
        "destaques": destaques,
        "recentes": recentes,
        "categorias": Categoria.objects.all()
    })


def painel(request):
    return render(request, "web/painel.html", {
        "total_receitas": Receita.objects.count(),
        "total_usuarios": Usuario.objects.count(),
        "total_categorias": Categoria.objects.count(),
    })


def contato(request):
    return render(request, "web/contato.html")


def login(request):
    return render(request, "web/login.html")


def receita(request):
    return render(request, "web/receita.html")
