from django.urls import path
from . import views

app_name = 'web'

urlpatterns = [
    path('', views.index, name='index'),
    path('receita/', views.receita, name='receita'),
    path('contato/', views.contato, name='contato'),
    path('login/', views.login, name='login'),
    path('painel/', views.painel, name='painel'),
]