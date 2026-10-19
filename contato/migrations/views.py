from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Contato




def contato_view(request):
   if request.method == 'POST':
       nome = request.POST.get('nome')
       email = request.POST.get('email')
       mensagem = request.POST.get('mensagem')


       if nome and email and mensagem:
           Contato.objects.create(
               nome=nome,
               email=email,
               mensagem=mensagem
           )
           messages.success(request, 'Mensagem enviada com sucesso!')
           return redirect('contato')


   return render(request, 'contato/contato.html')
