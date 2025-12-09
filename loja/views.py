from django.shortcuts import render, get_object_or_404, redirect
from .models import Colecao, Produto, Cupom
from django.contrib.auth.decorators import login_required
from .forms import ProdutoForm, ColecaoForm
from django.contrib import messages
from django.http import JsonResponse
from .forms import CupomForm

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
    cupons = Cupom.objects.all().order_by('-id')
    

    context = {
        'produtos': produtos,
        'cupons': cupons
        # 'colecoes': colecoes
    }
    return render(request, 'loja/dashboard.html', context)

@login_required(login_url='/admin/login/')
def produto_criar(request):
    if request.method == 'POST':
        form = ProdutoForm(request.POST, request.FILES) # request.FILES é obrigatório para upload de imagens
        if form.is_valid():
            form.save()
            return redirect('dashboard') # Volta para o painel depois de salvar
    else:
        form = ProdutoForm()
    
    return render(request, 'loja/produto_form.html', {'form': form, 'titulo': 'Novo Produto'})

# 2. EDITAR PRODUTO
@login_required(login_url='/admin/login/')
def produto_editar(request, id):
    produto = get_object_or_404(Produto, id=id) # Pega o produto ou dá erro 404 se não existir
    
    if request.method == 'POST':
        form = ProdutoForm(request.POST, request.FILES, instance=produto) # 'instance' carrega os dados atuais
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = ProdutoForm(instance=produto)
    
    return render(request, 'loja/produto_form.html', {'form': form, 'titulo': 'Editar Produto'})

# 3. REMOVER PRODUTO
@login_required(login_url='/admin/login/')
def produto_remover(request, id):
    produto = get_object_or_404(Produto, id=id)
    produto.delete()
    return redirect('dashboard')

def lista_produtos(request):
    colecoes = Colecao.objects.prefetch_related('produtos').all()
    
    return render(request, 'loja/produtos.html', {'colecoes': colecoes})

@login_required(login_url='/admin/login/')
def colecao_criar(request):
    if request.method == 'POST':
        form = ColecaoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard') 
    else:
        form = ColecaoForm()
    
    return render(request, 'loja/colecao_form.html', {'form': form})

@login_required(login_url='/admin/login/')
def colecao_criar(request):
    if request.method == 'POST':
        form = ColecaoForm(request.POST)
        if form.is_valid():
            colecao = form.save()  # Salva e guarda o objeto na variável 'colecao'
            
            # 2. Adicione esta linha:
            messages.success(request, f'Coleção "{colecao.nome}" criada com sucesso!')
            
            return redirect('dashboard')
    else:
        form = ColecaoForm()
    
    return render(request, 'loja/colecao_form.html', {'form': form})


def validar_cupom(request):
    codigo = request.GET.get('codigo')
    try:
        cupom = Cupom.objects.get(codigo__iexact=codigo, ativo=True)
        return JsonResponse({
            'valido': True,
            'desconto': cupom.desconto_porcentagem,
            'mensagem': f'Cupom de {cupom.desconto_porcentagem}% aplicado!'
        })
    except Cupom.DoesNotExist:
        return JsonResponse({
            'valido': False,
            'mensagem': 'Cupom inválido ou expirado.'
        })
    


@login_required(login_url='/admin/login/')
def cupom_criar(request):
    if request.method == 'POST':
        form = CupomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = CupomForm()
    
    return render(request, 'loja/cupom_form.html', {'form': form, 'titulo': 'Novo Cupom'})

@login_required(login_url='/admin/login/')
def cupom_remover(request, id):
    cupom = get_object_or_404(Cupom, id=id)
    cupom.delete()
    return redirect('dashboard')