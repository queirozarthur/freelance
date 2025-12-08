from django.shortcuts import render
from .models import Produto

def home(request):
    produtos = Produto.objects.filter(ativo=True)
    return render(request, 'loja/home.html', {'produtos': produtos})