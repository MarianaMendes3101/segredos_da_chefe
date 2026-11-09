from django.shortcuts import get_object_or_404, render
from .models import Receita


def index(request):
   destaques = Receita.objects.all()
   context = {
       'destaques': destaques
   }
   return render(request, 'receitas/index.html', context)


def home_view(request):
   return index(request)


def receitas_view(request):
   return render(request, 'receitas/receita.html')


def receita(request, id):
   receita_unica = get_object_or_404(Receita, pk=id)
   context = {
       'receita': receita_unica
   }
   return render(request, 'receitas/receita.html', context)


def detalhe_receita(request, receita_id):
 receita = get_object_or_404(Receita, pk=receita_id)
 context = {'receita': receita}
 return render(request, 'receitas/detalhe_receita.html', context)




from django.shortcuts import render, get_object_or_404
from .models import Receita, Categoria




# ... (mantenha as outras views que você já tem)


from django.shortcuts import render, get_object_or_404
from .models import Receita, Categoria




from django.shortcuts import render
from .models import Receita, Categoria


def receitas_view(request):
   receitas = Receita.objects.all().order_by('-id')
   categorias = Categoria.objects.all()


   # Captura o parâmetro 's' (ou 'busca' por segurança) enviado pelo formulário
   termo = request.GET.get('s') or request.GET.get('busca')
   if termo:
       receitas = receitas.filter(titulo__icontains=termo)


   # Filtro opcional por categoria, caso sua página de listagem use
   categoria_slug = request.GET.get('categoria')
   if categoria_slug:
       receitas = receitas.filter(categoria__slug=categoria_slug)


   context = {
       'receitas': receitas,
       'categorias': categorias,
   }
   return render(request, 'receitas/receita.html', context)
