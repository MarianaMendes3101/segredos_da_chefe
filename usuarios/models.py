from django.db import models

# Create your models here.
# usuarios/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models


class Usuario(AbstractUser):
   SEXO_CHOICES = [
       ('masculino', 'Masculino'),
       ('feminino', 'Feminino'),
       ('outro', 'Outro / Prefiro não informar'),
   ]


   sexo = models.CharField('Sexo', max_length=20, choices=SEXO_CHOICES, blank=True, null=True)
   data_nascimento = models.DateField('Data de Nascimento', blank=True, null=True)


   class Meta:
       verbose_name = 'Usuário'
       verbose_name_plural = 'Usuários'


   def __str__(self):
       return self.get_full_name() or self.username or self.email


