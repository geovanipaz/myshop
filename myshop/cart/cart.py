from decimal import Decimal
from django.conf import settings
from shop.models import Produto

class Carrinho(object):
    
    def __init__(self, request):
        '''
        inicializa o carrinho
        '''
        self.session = request.session
        carrinho = self.session.get(settings.CART_SESSION_ID)
        if not carrinho:
            #salva um carrinho vazio na sessão
            carrinho = self.session[settings.CART_SESSION_ID] = {}
        self.carrinho = carrinho
        
    def add(self, produto, quantidade = 1, substituir_quantidade=False):
        '''
        adicionar produto ao carrinho ou atualizar quantidade
        '''
        produto_id = str(produto.id)
        if produto_id not in self.carrinho:
            self.carrinho[produto_id] = {'quantidade':0,
                                         'preço':str(produto.preco)}
        
        if substituir_quantidade:
            self.carrinho[produto_id]['quantidade'] = quantidade
        else:
            self.carrinho[produto_id]['quantidade'] += quantidade
        self.save()
        
    def save(self):
        #marque a sessão como "modificada" para garantir que ela seja salva
        self.session.modified = True
        
    def remove(self, produto):
        '''
        remove o produto do carrinho
        '''
        produto_id = str(produto.id)
        if produto_id in self.carrinho:
            del self.carrinho[produto_id]
            self.save()
            
    def __iter__(self):
        '''
        Iterar sobre os itens no carrinho e obter os produtos
        do banco de dados.
        '''
        produto_ids = self.carrinho.keys()
        #pegue os objetos do produto e adicione-os ao carrinho
        produtos = Produto.objects.filter(id__in=produto_ids)
        carrinho = self.carrinho.copy()
        
        for produto in produtos:
            carrinho[str(produto.id)]['produto'] = produto
            
        for item in carrinho.values():
            item['preco'] = Decimal(item['preco'])
            item['preco_total'] = item['preco'] * item['quantidade']
            yield item
            
    def __len__(self):
        '''
        contagem de itens no carrinho
        '''
        return sum(item['quantidade'] for item in self.carrinho.values)
    
    def get_total_preco(self):
        return sum(Decimal(item['preco'])* item['quantidade'] for item in 
                   self.carrinho.values())
    def clear(self):
        #remove o carrinho da sessão
        del self.session[settings.CART_SESSION_ID]
        self.save()