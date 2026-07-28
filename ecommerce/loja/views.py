from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Sessão de Compra.
def home(request):
    return render(request, 'home.html')

def loja(request):
    produtos = Produto.objects.all()
    return render(request, 'loja.html', context={'produtos': produtos})

def carrinho(request):
    return render(request, 'carrinho.html')

def checkout(request):
    return render(request, 'checkout.html')

#Sessao de login
def minha_conta(request):
    return render(request, 'usuario/home.html')

def login(request):
    return render(request, 'usuario/login.html')