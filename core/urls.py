from django.urls import path
from . import views

urlpatterns = [
    # Mapeia a página inicial do app core para a função index (ou o nome da sua view)
    path('', views.index, name='index'),
]