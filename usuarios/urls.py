from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path, reverse_lazy
from . import views

app_name = "usuarios"
urlpatterns = [
    path("login/", LoginView.as_view(template_name="usuarios/login.html", redirect_authenticated_user=True), name="login"),
    path("logout/", LogoutView.as_view(next_page=reverse_lazy("web:index")), name="logout"),
    path("cadastro/", views.cadastro, name="cadastro"),
    path("", views.lista_usuarios, name="lista"),
    path("<int:pk>/editar/", views.editar_usuario, name="editar"),
    path("<int:pk>/excluir/", views.excluir_usuario, name="excluir"),
]
