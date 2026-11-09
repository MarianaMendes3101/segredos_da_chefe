# receitas/models.py
from django.db import models


class Categoria(models.Model):
   nome = models.CharField('Nome da Categoria', max_length=100)
   slug = models.SlugField('Slug / URL', unique=True)
   ordem = models.PositiveIntegerField('Ordem de exibição', default=1, help_text="Ex: 1 para 01, 2 para 02")


   class Meta:
       verbose_name = 'Categoria'
       verbose_name_plural = 'Categorias'
       ordering = ['ordem']


   def __str__(self):
       return f"{self.ordem:02d} - {self.nome}"




class Receita(models.Model):
   OCASIOES = [
       ('cafe', 'Café da manhã'),
       ('almoco_jantar', 'Almoço ou Jantar'),
       ('sobremesa', 'Sobremesa'),
       ('lanche', 'Lanches'),
   ]


   titulo = models.CharField('Título da Receita', max_length=150)
   slug = models.SlugField('Slug / URL', unique=True)
   tempo_preparo = models.CharField('Tempo de Preparo', max_length=30, help_text="Ex: 25 min")
   descricao = models.TextField('Descrição Curta', help_text="Texto exibido nos cards da Home e do Carrossel")
   ingredientes = models.TextField('Ingredientes', blank=True, help_text="Separe os ingredientes por linha")
   modo_preparo = models.TextField('Modo de Preparo', blank=True, help_text="Passo a passo do preparo")
   imagem = models.ImageField('Imagem da Receita', upload_to='receitas/')
   categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name='receitas', verbose_name='Categoria')
   ocasiao = models.CharField('Ocasião de Consumo', max_length=50, choices=OCASIOES, blank=True, null=True)
   destaque = models.BooleanField('Exibir na Home (Destaque)', default=False)
   criado_em = models.DateTimeField('Cadastrado em', auto_now_add=True)


   class Meta:
       verbose_name = 'Receita'
       verbose_name_plural = 'Receitas'
       ordering = ['-criado_em']


   def __str__(self):
       return self.titulo
