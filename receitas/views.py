from django.shortcuts import render, get_object_or_404
from .models import Receita, Categoria


def index(request):
   destaques = Receita.objects.all()

   context = {
       'destaques': destaques
   }
   return render(request, 'web/index.html', context)


def home_view(request):
   return index(request)


def receitas_view(request):
    receitas = Receita.objects.all().order_by('-id')
    categorias = Categoria.objects.all()

    # Busca por título
    termo = request.GET.get('s') or request.GET.get('busca')

    if termo:
        receitas = receitas.filter(titulo__icontains=termo)

    # Filtro por categoria
    categoria_slug = request.GET.get('categoria')

    if categoria_slug:
        receitas = receitas.filter(categoria__slug=categoria_slug)

    context = {
        'receitas': receitas,
        'categorias': categorias,
    }

    return render(request, 'web/receita.html', context)


def receita(request, id):
   receita_unica = get_object_or_404(Receita, pk=id)
   context = {
       'receita': receita_unica
   }
   return render(request, 'web/receita.html', context)


