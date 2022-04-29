from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'shop'

urlpatterns = [
    path('', views.lista_produtos, name='lista_produtos'),
    path('<slug_categoria>/', views.lista_produtos, name='lista_produtos_categoria'),
    path('<id>/<slug>/', views.detalhe_produto, name='detalhe_produto')
]
