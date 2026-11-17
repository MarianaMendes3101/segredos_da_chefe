from django.db import models


class Contato(models.Model):
    nome = models.CharField("Nome", max_length=100)
    email = models.EmailField("E-mail")
    mensagem = models.TextField("Mensagem")
    data_envio = models.DateTimeField("Data de envio", auto_now_add=True)

    class Meta:
        verbose_name = "Mensagem de contato"
        verbose_name_plural = "Mensagens de contato"
        ordering = ["-data_envio"]

    def __str__(self):
        return f"{self.nome} - {self.email}"
