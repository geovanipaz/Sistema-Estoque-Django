from dataclasses import field, fields
from pyexpat import model
from django import forms

from .models import Estoque, HistoricoEstoque

class EstoqueCreateForm(forms.ModelForm):
    class Meta:
        model = Estoque
        fields = ['categoria','item_nome','quantidade']
    
    def clean_categoria(self):
        categoria = self.cleaned_data.get('categoria')
        if not categoria:
            raise forms.ValidationError('Este campo é requerido')
        
        for estoque in Estoque.objects.all():
            if estoque.categoria == categoria:
                raise forms.ValidationError(str(categoria)+' já foi criada')
        return categoria
    
    def clean_item_nome(self):
        item_nome = self.cleaned_data.get('item_nome')
        if not item_nome:
            raise forms.ValidationError('Este campo é requerido')
        return item_nome
		
        
class EstoqueSearchForm(forms.ModelForm):
    exportar_para_CSV = forms.BooleanField()
    class Meta:
        model = Estoque
        fields = ['categoria', 'item_nome']        
        
class EstoqueUpdateForm(forms.ModelForm):
    class Meta:
        model = Estoque
        fields = ['categoria','item_nome', 'quantidade']
        
class EmitirForm(forms.ModelForm):
    class Meta:
        model = Estoque
        fields = ['quantidade_emitida', 'emitida_para']

class ReceberForm(forms.ModelForm):
    class Meta:
        model = Estoque
        fields = ['quantidade_recebida', 'emitida_por']
        
class NivelReabastecimentoForm(forms.ModelForm):
    class Meta:
        model = Estoque
        fields = ['nivel_reabastecimento']
        
class HistoricoEstoqueSearchForm(forms.ModelForm):
    exportar_para_CSV = forms.BooleanField(required=False)
    data_inicio = forms.DateTimeField(required=False)
    data_fim = forms.DateTimeField(required=False)
    class Meta:
        model = HistoricoEstoque
        fields = ['categoria', 'item_nome', 'data_inicio', 'data_fim']
        