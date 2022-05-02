import django
from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.http import require_POST
from shop.models import Produto
from .cart import Carrinho
from cart.forms import AddProdutoCarrinhoForm


# Create your views here.

@require_POST
def adiciona_carrinho(request, produto_id):
    carrinho = Carrinho(request)
    produto = get_object_or_404(Produto, id =produto_id)
    form = AddProdutoCarrinhoForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        carrinho.add(produto=produto,
                     quantidade=cd['quantidade'],
                     substituir_quantidade=cd['sobrepor'])
    return redirect('cart:cart_detail')
    
@require_POST
def deleta_do_carrinho(request, produto_id):
    carrinho = Carrinho(request)
    produto = get_object_or_404(Produto, id=produto_id)
    carrinho.remove(produto)
    return redirect('cart:cart_detail')

def carrinho_detail(request):
    carrinho = Carrinho(request)
    return render(request, 'cart/cart_detail.html', {'carrinho':carrinho})
