from django.shortcuts import render
from django.http import HttpResponse

# Sessão de Compra.
def home(request):
    return render(request, 'home.html')

def loja(request):
    return render(request, 'loja.html')

def carrinho(request):
    return render(request, 'carrinho.html')

def checkout(request):
    return render(request, 'checkout.html')

#Sessao de login
def minha_conta(request):
    return render(request, 'usuario/home.html')

def login(request):
    return render(request, 'usuario/login.html')