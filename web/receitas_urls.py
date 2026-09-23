from django.urls import path
from . import views

app_name = 'receitas'

urlpatterns = [
    path('', views.index, name='index'),
    path('receitas/', views.receitas_view, name='receitas_lista'),
    path('receita/<int:id>/', views.receita, name='receita'),
]