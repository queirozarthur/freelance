from django.contrib import admin
from .models import Colecao, Produto, ProdutoVariacao, Tamanho, Cupom


class VariacaoInline(admin.TabularInline):
    model = ProdutoVariacao
    extra = 1

@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    inlines = [VariacaoInline]
    list_display = ('nome', 'colecao', 'preco', 'ativo')

@admin.register(Cupom)
class CupomAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'desconto_porcentagem', 'ativo')
    search_fields = ('codigo',)

admin.site.register(Colecao)
admin.site.register(Tamanho)