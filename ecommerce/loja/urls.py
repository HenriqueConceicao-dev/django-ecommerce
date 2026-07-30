from django.urls import path

from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('loja/', loja, name='loja'),
    path('loja/<str:nome_categoria>/', loja, name='loja'),
    path('produto/<int:id_produto>/', ver_produto, name='ver_produto'),
    path('carrinho/', carrinho, name='carrinho'),
    path('checkout/', checkout, name='checkout'),
    path('minhaconta/', minha_conta, name='minha_conta'),
    path('login/', login, name='login'),
]
