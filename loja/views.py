from django.shortcuts import render, get_object_or_404
from .models import Colecao, Produto

def home(request):
    colecoes = Colecao.objects.filter(ativa=True).prefetch_related('produtos')
    return render(request, 'loja/home.html', {'colecoes': colecoes})

# Nova função: Detalhes do Produto
def produto_detail(request, id):
    produto = get_object_or_404(Produto, id=id)
    # Pega as variações (P, M, G) desse produto
    variacoes = produto.variacoes.filter(estoque_disponivel=True)
    return render(request, 'loja/produto_detail.html', {
        'produto': produto,
        'variacoes': variacoes
    })