from django import forms
from django.shortcuts import render, get_object_or_404
from .models import Categoria, Produto
from cart.forms import AddProdutoCarrinhoForm
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
    produto = get_object_or_404(Produto,  slug=slug, disponivel=True)
    carrinho_produto_form = AddProdutoCarrinhoForm()
    return render(request, 'shop/detail.html', {'produto':produto,
                                                'carrinho_produto_form':carrinho_produto_form})