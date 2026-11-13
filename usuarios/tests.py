from django.test import TestCase
from django.urls import reverse
from .models import Usuario


class CadastroUsuarioTests(TestCase):
    def test_criar_conta(self):
        response = self.client.post(reverse("usuarios:cadastro"), {
            "username": "aluna_teste", "first_name": "Aluna", "last_name": "Teste",
            "email": "aluna@example.com", "password1": "M7!qZ2@vP9#x", "password2": "M7!qZ2@vP9#x",
            "sexo": "feminino", "data_nascimento": "2008-01-01",
        })
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Usuario.objects.filter(username="aluna_teste").exists())
