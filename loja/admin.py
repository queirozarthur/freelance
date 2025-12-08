from django.contrib import admin
from .models import Colecao, Produto, ProdutoVariacao, Tamanho


class VariacaoInline(admin.TabularInline):
    model = ProdutoVariacao
    extra = 1

@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    inlines = [VariacaoInline]
    list_display = ('nome', 'colecao', 'preco', 'ativo')

admin.site.register(Colecao)
admin.site.register(Tamanho)