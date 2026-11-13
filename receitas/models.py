from django.db import models


class Categoria(models.Model):
    nome = models.CharField('Nome da Categoria', max_length=100)
    slug = models.SlugField('Slug / URL', unique=True)
    ordem = models.PositiveIntegerField('Ordem', default=0)

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        ordering = ['ordem']

    def __str__(self):
        return f"{self.ordem:02d} - {self.nome}"


class Receita(models.Model):
    titulo = models.CharField('Título', max_length=150)
    slug = models.SlugField('Slug / URL', unique=True)
    tempo_preparo = models.CharField('Tempo de Preparo', max_length=30)
    ingredientes = models.TextField('Ingredientes', blank=True)
    modo_preparo = models.TextField('Modo de Preparo', blank=True)
    imagem = models.ImageField(
        'Imagem da Receita',
        upload_to='receitas/',
        blank=True,
        null=True
    )
    categoria = models.ForeignKey(
        Categoria,
        on_delete=models.CASCADE,
        related_name='receitas',
        verbose_name='Categoria'
    )
    destaque = models.BooleanField(
        'Exibir na Home (Destaque)',
        default=False
    )
    criado_em = models.DateTimeField('Cadastrado em', auto_now_add=True)

    class Meta:
        verbose_name = 'Receita'
        verbose_name_plural = 'Receitas'
        ordering = ['-criado_em']

    def __str__(self):
        return self.titulo