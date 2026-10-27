# Create your views here.
from django.shortcuts import render


def index(request):
    return render(request, 'web/index.html')
def painel(request):
    return render(request, 'web/painel.html')
def contato(request):
    return render(request, 'web/contato.html')
def login(request):
    return render(request, 'web/login.html')
def receita(request):
    return render(request, 'web/receita.html')