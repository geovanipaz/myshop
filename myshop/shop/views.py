from django.shortcuts import render, get_object_or_404
from .models import Categoria, Produto
# Create your views here.

def lista_produtos(request, slug_categoria = None):
    categoria = None
    categorias = Categoria.objects.all()
    produtos = Produto.objects.filter(disponivel=True)
    if slug_categoria:
        categoria = get_object_or_404(Categoria, slug=slug_categoria)
        produtos = produtos.filter(categoria=categoria)
    return render(request, 'shop/list.html',
                  {'categoria':categoria,
                   'categorias': categorias,
                   'produtos':produtos})
    
def detalhe_produto(request, id, slug):
    produto = get_object_or_404(Produto, id=id, slug=slug, disponivel=True)
    return render(request, 'shop/detalhe.html', {'produto':produto})