from django import forms
from .models import Produto, Colecao, Tamanho, Cupom

class ProdutoForm(forms.ModelForm):
    tamanhos = forms.ModelMultipleChoiceField(
        queryset=Tamanho.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False,
        label="Tamanhos Disponíveis"
    )

    class Meta:
        model = Produto
        fields = ['colecao','nome', 'preco', 'descricao', 'foto_principal', 'ativo','tamanhos',] 
        

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'w-full px-4 py-3 rounded-lg bg-gray-50 border border-gray-300 focus:border-blue-500 focus:bg-white focus:ring-2 focus:ring-blue-200 text-gray-900 transition duration-200 outline-none'
            field.widget.attrs['placeholder'] = f'Digite {field.label.lower()}...'
        self.fields['tamanhos'].widget.attrs['class'] = 'flex flex-wrap gap-4 mt-2'

class ColecaoForm(forms.ModelForm):
    class Meta:
        model = Colecao
        fields = ['nome'] 

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'w-full px-4 py-3 rounded-lg bg-gray-50 border border-gray-300 focus:border-blue-500 focus:bg-white focus:ring-2 focus:ring-blue-200 text-gray-900 transition duration-200 outline-none'
            field.widget.attrs['placeholder'] = f'Digite {field.label.lower()}...'

class CupomForm(forms.ModelForm):
    class Meta:
        model = Cupom
        fields = ['codigo', 'desconto_porcentagem', 'ativo']
        labels = {
            'codigo': 'Código do Cupom (Ex: VERAO10)',
            'desconto_porcentagem': 'Porcentagem de Desconto',
            'ativo': 'Cupom Ativo?'
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if field_name != 'ativo': 
                field.widget.attrs['class'] = 'w-full px-4 py-3 rounded-lg bg-gray-50 border border-gray-300 focus:border-black focus:bg-white focus:ring-0 text-gray-900 transition duration-200 outline-none uppercase'