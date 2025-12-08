from django.shortcuts import render, get_object_or_404
from .models import Colecao, Produto

def home(request):
    colecoes = Colecao.objects.filter(ativa=True).prefetch_related('produtos')
    return render(request, 'loja/home.html', {'colecoes': colecoes})


def produto_detail(request, id):
    produto = get_object_or_404(Produto, id=id)
    variacoes = produto.variacoes.filter(estoque_disponivel=True)
    return render(request, 'loja/produto_detail.html', {
        'produto': produto,
        'variacoes': variacoes
    })

def sobre(request):

    context = {
        'titulo_pagina': 'Sobre Nós - Minha Loja'
    }
    return render(request, 'sobre.html', context)