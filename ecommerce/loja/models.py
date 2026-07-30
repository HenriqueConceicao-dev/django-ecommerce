from django.db import models
from django.contrib.auth.models import User

# Banco de Dados
class Cliente(models.Model):
    nome = models.CharField(max_length=255, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    telefone = models.CharField(max_length=11, null=True, blank=True)
    id_sessao = models.CharField(max_length=255, null=True, blank=True)
    usuario = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)

#-------------- TABELA RELECIONADO A PRODUTO
#categoria - masculino, feminino, infatil.
class Categoria(models.Model):
    nome = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.nome


# Tipo - exemplo (camisa, bermunda, calça, etc)
class Tipo(models.Model):
    nome = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
            return self.nome

class Produto(models.Model):
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True, blank=True)
    tipo = models.ForeignKey(Tipo, on_delete=models.SET_NULL, null=True, blank=True)

    imagem = models.ImageField(null=True, blank=True)
    nome = models.CharField(max_length=255, null=True, blank=True)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    ativo = models.BooleanField(default=True)

    def __str__(self):
                return f'{self.nome} - {self.preco}'

#----------------- FIM  PRODUTO

#-------------- TABELA RELECIONADO A PEDIDO
class ItemEstoque(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.SET_NULL, null=True, blank=True )
    cor = models.CharField(max_length=255, null=True, blank=True)
    tamanho = models.CharField(max_length=255, null=True, blank=True)
    quantidade = models.IntegerField(default=0)

class Endereco(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    
    rua = models.CharField(max_length=255, null=True, blank=True)
    numero = models.IntegerField()
    complemento = models.CharField(max_length=255, null=True, blank=True)
    cep = models.CharField(max_length=50, null=True, blank=True)
    cidade = models.CharField(max_length=255, null=True, blank=True)
    estado = models.CharField(max_length=255, null=True, blank=True)

class Pedido(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.SET_NULL, null=True, blank=True)

    finalizado = models.BooleanField(default=False)
    data_finalizacao = models.DateTimeField()
    codigo_transacao = models.CharField()
    endereco = models.ForeignKey(Endereco, on_delete=models.SET_NULL, null=True, blank=True )


class ItemPedido(models.Model):
    item_estoque = models.ForeignKey(ItemEstoque, on_delete=models.SET_NULL, null=True, blank=True)
    quantidade = models.IntegerField(default=0)
    item_estoque = models.ForeignKey(Pedido, on_delete=models.SET_NULL, null=True, blank=True)
#----------------- FIM  PEDIDO

class Banner(models.Model):
     imagem = models.ImageField(null=True, blank=True)
     link_destino = models.CharField(max_length=255, null=True, blank=True)
     ativo = models.BooleanField(default=False)

     def __str__(self):
          return str(f"{self.link_destino} - {self.ativo}")