from django.db import models

class Colecao(models.Model):
    nome = models.CharField(max_length=100)
    imagem_capa = models.ImageField(upload_to='colecoes/')
    ativa = models.BooleanField(default=True)

    def __str__(self):
        return self.nome

class Tamanho(models.Model):
    nome = models.CharField(max_length=5) # Ex: P, M, G, 40, 42
    
    def __str__(self):
        return self.nome

class Produto(models.Model):
    colecao = models.ForeignKey(Colecao, on_delete=models.CASCADE, related_name='produtos')
    nome = models.CharField(max_length=200)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    foto_principal = models.ImageField(upload_to='produtos/')
    descricao = models.TextField(blank=True, null=True)
    ativo = models.BooleanField(default=True)
    tamanhos = models.ManyToManyField(Tamanho, blank=True, related_name='produtos')

    def __str__(self):
        return self.nome

class ProdutoVariacao(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE, related_name='variacoes')
    tamanho = models.CharField(max_length=10) # Ex: P, M, G, 42
    estoque_disponivel = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.produto.nome} - {self.tamanho}"
    
