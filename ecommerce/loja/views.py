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

def ver_produto(request, id_produto):
    produto = Produto.objects.get(id=id_produto)
    return render(request, 'ver_produto.html', context={'produto':produto})

def carrinho(request):
    return render(request, 'carrinho.html')

def checkout(request):
    return render(request, 'checkout.html')

#Sessao de login
def minha_conta(request):
    return render(request, 'usuario/home.html')

def login(request):
    return render(request, 'usuario/login.html')