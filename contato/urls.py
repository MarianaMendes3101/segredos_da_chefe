from django.urls import path
from . import views

app_name = "contato"
urlpatterns = [
    path("", views.criar_contato, name="criar"),
    path("mensagens/", views.lista_contatos, name="lista"),
    path("mensagens/<int:pk>/editar/", views.editar_contato, name="editar"),
    path("mensagens/<int:pk>/excluir/", views.excluir_contato, name="excluir"),
]
