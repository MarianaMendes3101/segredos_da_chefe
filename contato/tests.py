from django.test import TestCase
from django.urls import reverse
from .models import Contato


class CadastroContatoTests(TestCase):
    def test_enviar_mensagem(self):
        response = self.client.post(reverse("contato:criar"), {
            "nome": "Ana Silva", "email": "ana@example.com", "mensagem": "Olá, gostei do site!"
        })
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Contato.objects.filter(email="ana@example.com").exists())

    def test_email_invalido_nao_salva(self):
        response = self.client.post(reverse("contato:criar"), {
            "nome": "Ana Silva", "email": "email-invalido", "mensagem": "Olá"
        })
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Contato.objects.count(), 0)
