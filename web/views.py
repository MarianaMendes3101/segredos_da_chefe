from django.shortcuts import render

# Create your views here.
from django.shortcuts import render


def home(request):
    return render(request, 'web/index.html')
def painel(request):
    return render(request, 'web/painel.html')