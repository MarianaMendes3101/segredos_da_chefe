from django.urls import path
from . import views

app_name = "receitas"
urlpatterns = [
    path("", views.ReceitaListView.as_view(), name="receita_list"),
    path("cadastrar/", views.ReceitaCreateView.as_view(), name="receita_create"),
    path("<int:pk>/", views.ReceitaDetailView.as_view(), name="receita_detail"),
    path("<int:pk>/editar/", views.ReceitaUpdateView.as_view(), name="receita_update"),
    path("<int:pk>/excluir/", views.ReceitaDeleteView.as_view(), name="receita_delete"),
    path("categorias/", views.CategoriaListView.as_view(), name="categoria_list"),
    path("categorias/cadastrar/", views.CategoriaCreateView.as_view(), name="categoria_create"),
    path("categorias/<int:pk>/editar/", views.CategoriaUpdateView.as_view(), name="categoria_update"),
    path("categorias/<int:pk>/excluir/", views.CategoriaDeleteView.as_view(), name="categoria_delete"),
]
