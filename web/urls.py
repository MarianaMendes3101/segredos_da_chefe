from django.urls import path
from . import views

app_name = 'web'

urlpatterns = [
    path('', views.home, name='index'),
    path('receita/', views.receita, name='receita'),
    path('painel/', views.painel, name='painel'),
]