
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views
from .forms import EmailAuthenticationForm

app_name = "usuarios"

urlpatterns = [
    path("cadastro/", views.cadastro, name="cadastro"),

    path(
        "login/",
        LoginView.as_view(
            template_name="usuarios/login.html",
            authentication_form=EmailAuthenticationForm,
        ),
        name="login"
    ),

    path("logout/", LogoutView.as_view(), name="logout"),

    path("", views.UsuarioListView.as_view(), name="lista"),

    path(
        "cadastrar/",
        views.UsuarioCreateView.as_view(),
        name="criar"
    ),

    path(
        "<int:pk>/editar/",
        views.UsuarioUpdateView.as_view(),
        name="editar"
    ),

    path(
        "<int:pk>/excluir/",
        views.UsuarioDeleteView.as_view(),
        name="excluir"
    ),
]
