from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name='Nome')
    description = models.TextField(null=True, blank=True, verbose_name='Descrição')

    class Meta:
        verbose_name = 'Categoria'

    def __str__(self):
        return self.name

# Create your models here.
# Django ORM - Object Relational Mapper
class Post(models.Model):
    title = models.CharField(max_length=255, verbose_name='Título')
    # null para DB
    # blank para admin
    subtitle = models.CharField(max_length=255, null=True, blank=True, verbose_name='Sub-título')
    content = models.TextField(verbose_name='Conteúdo')
    author = models.ForeignKey(User, on_delete=models.PROTECT)
    categories = models.ManyToManyField(Category)

    class Meta:
        verbose_name = 'Artigo'
        #verbose_name_plural = 'Artigos'

    def __str__(self):
        return self.title

