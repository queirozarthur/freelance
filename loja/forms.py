from django import forms
from .models import Produto, Colecao, Tamanho

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