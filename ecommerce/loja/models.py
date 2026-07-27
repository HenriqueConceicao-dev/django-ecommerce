from django.db import models

# Banco de Dados
'''  
class Cliente(models.Model):
    nome = models.CharField(max_length=255)
    email = models.EmailField()
    telefone = models.CharField(max_length=12)

    
class Pedido(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    endereco = models.ForeignKey(Endereco, on_delete=models.CASCADE)

    codigo_pedido = models.IntegerField()
    data_finalizacao = models.DateTimeField()
    id_transacao = models.CharField()


    itens = models.CharField()
    preco = models.BooleanField()

class Endereco(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)

    rua = models.CharField(max_length=255)
    numero = models.CharField(max_length=255)
    complemento = models.CharField(max_length=255)
    cep = models.CharField(max_length=255)
    cidade = models.CharField(max_length=255)
    estado = models.CharField(max_length=255)


# ------- TABELAS QUE ENVOLVE O PRODUDUTO
class Produto(models.Model):
    categoria = models.ForeignKey(Categorias, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Tipos, on_delete=models.CASCADE)

    imagem_p = models.ImageField()
    nome = models.CharField(max_length=100)
    preco = models.BooleanField()
    ativo = models.CharField(max_length=100)

#categoria - masculino, feminino, infatil.
class Categorias(models.Model):
    nome = models.CharField(max_length=30)


# Tipo - exemplo (camisa, bermunda, calça, etc)
class Tipos(models.Model):
    nome = models.CharField(max_length=30)

class item_estoque(models.Model):
    Produto
    Cor
    Tamanho
    quantidade

class itensPedido(models.Model):
    item_estoque
    quantidade


# ------- FIM 

'''  