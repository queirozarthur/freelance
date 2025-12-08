from django.shortcuts import render, get_object_or_404
from .models import Colecao, Produto
from django.contrib.auth.decorators import login_required

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
    return render(request, 'loja/sobre.html', context)

def is_admin(user):
    return user.is_staff

@login_required(login_url='/admin/login/') 
def dashboard(request):

    if not request.user.is_staff:
        return redirect('home')

    produtos = Produto.objects.all().order_by('-id')
    
    # Se você tiver Coleção, busque aqui também:
    # colecoes = Colecao.objects.all() 

    context = {
        'produtos': produtos,
        # 'colecoes': colecoes
    }
    return render(request, 'loja/dashboard.html', context)