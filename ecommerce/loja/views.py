from django.shortcuts import render, redirect
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
    cor_selecionada = None

    if id_cor:
        cor_selecionada = Cor.objects.get(id=id_cor)

    produto = Produto.objects.get(id=id_produto)
    itens_estoque = ItemEstoque.objects.filter(produto=produto , quantidade__gt=0)

    if len(itens_estoque) > 0:#tem item no estoque
        tem_estoque = True
        cores = {item.cor for item in itens_estoque}
        if id_cor:
            itens_estoque = ItemEstoque.objects.filter(produto=produto , quantidade__gt=0, cor__id= id_cor)
            tamanhos = {item.tamanho for item in itens_estoque}

    return render(request, 'ver_produto.html', context={'produto':produto,'tem_estoque': tem_estoque, 'cores': cores, 'tamanhos':tamanhos,
                                                        'cor_selecionada':cor_selecionada,})
    

def adicionar_carrinho(request, id_produto):
    if request.method == "POST" and id_produto:
        dados = request.POST.dict()
        tamanho = dados.get('tamanho')
        cor = dados.get('cor')
        if not tamanho:
            return redirect('loja')
        #pegar o cliente
        # criar o pedido ou pegar o pedido que esta em aberto
        return HttpResponse(f'{id_produto}/ {tamanho} / {cor} adicionado')
    else: 
        return redirect('carrinho')


def carrinho(request):
    return render(request, 'carrinho.html')

def checkout(request):
    return render(request, 'checkout.html')

#Sessao de login
def minha_conta(request):
    return render(request, 'usuario/home.html')

def login(request):
    return render(request, 'usuario/login.html')