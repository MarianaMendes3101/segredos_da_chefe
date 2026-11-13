from django.test import TestCase
from django.urls import reverse
from .models import Categoria, Receita


class CadastroReceitasTests(TestCase):
    def setUp(self):
        self.categoria = Categoria.objects.create(nome="Categoria de teste", slug="categoria-de-teste", ordem=1)
        self.receita = Receita.objects.create(
            titulo="Bolo de teste", slug="bolo-de-teste", tempo_preparo="30 min",
            descricao="Uma receita de teste.", categoria=self.categoria,
        )

    def test_lista_receitas_abre(self):
        response = self.client.get(reverse("receitas:receita_list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Bolo de teste")

    def test_cadastro_receita(self):
        response = self.client.post(reverse("receitas:receita_create"), {
            "titulo": "Pudim de teste", "slug": "", "tempo_preparo": "40 min",
            "descricao": "Pudim caseiro.", "ingredientes": "Leite\nOvos", "modo_preparo": "Misture tudo.",
            "categoria": self.categoria.pk, "ocasiao": "sobremesa",
        })
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Receita.objects.filter(titulo="Pudim de teste", slug="pudim-de-teste").exists())

    def test_categoria_com_receitas_nao_pode_ser_excluida(self):
        response = self.client.post(reverse("receitas:categoria_delete", args=[self.categoria.pk]))
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Categoria.objects.filter(pk=self.categoria.pk).exists())

    def test_editar_receita(self):
        response = self.client.post(reverse("receitas:receita_update", args=[self.receita.pk]), {
            "titulo": "Bolo atualizado", "slug": "bolo-atualizado", "tempo_preparo": "35 min",
            "descricao": "Descrição atualizada", "ingredientes": "Farinha", "modo_preparo": "Asse.",
            "categoria": self.categoria.pk, "ocasiao": "sobremesa",
        })
        self.assertEqual(response.status_code, 302)
        self.receita.refresh_from_db()
        self.assertEqual(self.receita.titulo, "Bolo atualizado")
