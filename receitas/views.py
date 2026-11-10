from django.http import request
from django.shortcuts import render, get_object_or_404
from .models import Receita, Categoria
from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render, redirect
from .models import Receita

# Função auxiliar para verificar se o usuário é Administrador/Staff
def is_admin(user):
    return user.is_authenticated and user.is_staff
@user_passes_test(is_admin, login_url='/login/')
def cadastrar_receita(request):
    if request.method == 'POST':
        # Lógica para salvar a receita no banco de dados
        pass
    return render(request, 'web/cadastrar_receita.html')

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


