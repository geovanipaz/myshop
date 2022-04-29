from tkinter.tix import Tree
from django.db import models
from django.urls import reverse

class Categoria(models.Model):
    nome = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, unique=True)
    
    class Meta:
        ordering = ('nome',)
        verbose_name = 'categoria'
        verbose_name_plural = 'categorias'
    def __str__(self) -> str:
        return self.nome
    
    def get_absolute_url(self):
        return reverse("shop:lista_produtos_categoria", args=[self.slug])
    


class Produto(models.Model):
    categoria = models.ForeignKey(Categoria, related_name='produtos',
                                  on_delete=models.CASCADE)
    nome = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True)
    imagem = models.ImageField(upload_to='produtos/%Y/%m/%d', blank=True)
    descricao = models.TextField(blank=True)
    preco = models.DecimalField(max_digits=10,decimal_places=2)
    disponivel = models.BooleanField(default=True)
    criado = models.DateTimeField(auto_now_add=True)
    atualizado = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ('nome',)
        index_together = (('id','slug'))
        
    def __str__(self) -> str:
        return self.nome
    def get_absolute_url(self):
        return reverse("shop:detalhe_produto", args=[self.id,self.slug])