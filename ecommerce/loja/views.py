from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Sessão de Compra.
def home(request):
    banners = Banner.objects.filter(ativo=True)
    return render(request, 'home.html', context={'banners': banners} )

def loja(request, nome_categoria=None):
    produtos = Produto.objects.filter(ativo=True)  
    if nome_categoria:
        produtos = Produto.objects.filter(ativo=True,categoria__nome=nome_categoria)  
    return render(request, 'loja.html', context={'produtos': produtos})

def ver_produto(request, id_produto,id_cor=None):
    tem_estoque = False
    cores = {}
    tamanhos = {}
    nome_cor_selecionada = None

    if id_cor:
        cor = Cor.objects.get(id=id_cor)
        nome_cor_selecionada = cor.nome

    produto = Produto.objects.get(id=id_produto)
    itens_estoque = ItemEstoque.objects.filter(produto=produto , quantidade__gt=0)

    if len(itens_estoque) > 0:#tem item no estoque
        tem_estoque = True
        cores = {item.cor for item in itens_estoque}
        if id_cor:
            itens_estoque = ItemEstoque.objects.filter(produto=produto , quantidade__gt=0, cor__id= id_cor)
            tamanhos = {item.tamanho for item in itens_estoque}

    return render(request, 'ver_produto.html', context={'produto':produto, 'itens_estoque': itens_estoque,'tem_estoque': tem_estoque, 'cores': cores, 'tamanhos':tamanhos,
                                                        'nome_cor_selecionada':nome_cor_selecionada,})

def carrinho(request):
    return render(request, 'carrinho.html')

def checkout(request):
    return render(request, 'checkout.html')

#Sessao de login
def minha_conta(request):
    return render(request, 'usuario/home.html')

def login(request):
    return render(request, 'usuario/login.html')