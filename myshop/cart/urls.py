from django.urls import path
from . import views

app_name = 'cart'

urlpatterns = [
    path('', views.carrinho_detail, name='cart_detail'),
    path('add/<produto_id>/', views.adiciona_carrinho, name='cart_add'),
    path('remove/<produto_id>/', views.deleta_do_carrinho, name='cart_remove'),
]
