from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from datetime import datetime

User = get_user_model()

def login_view(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        sexo = request.POST.get('sexo')
        nascimento = request.POST.get('nascimento')

        # Exemplo básico de cadastro rápido pela tela de login
        if email and not User.objects.filter(email=email).exists():
            username = email.split('@')[0]
            user = User.objects.create_user(username=username, email=email, first_name=nome)
            user.sexo = sexo
            if nascimento:
                user.data_nascimento = datetime.strptime(nascimento, '%Y-%m-%d').date()
            user.save()

        return redirect('login')

    return render(request, 'usuarios/login.html')