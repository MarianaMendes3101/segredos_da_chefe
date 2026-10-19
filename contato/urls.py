from django.urls import path
from .views import contato_view


urlpatterns = [
   path('', contato_view, name='contato'),
]
