from django import forms
from .models import Epi

class EpiForm(forms.ModelForm):
    class Meta:
        model = Epi
        fields = ['nome_epi', 'descricao_epi', 'quantidade_total', 'quantidade_disponivel']
        labels = {
            'nome_epi': 'Nome do EPI',
            'descricao_epi': 'Descrição do EPI',
            'quantidade_total': 'Quantidade Total',
            'quantidade_disponivel': 'Quantidade Disponível',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['nome_epi'].widget.attrs.update({'class': 'form-control'})
        self.fields['descricao_epi'].widget.attrs.update({'class': 'form-control', 'rows': 3})
        self.fields['quantidade_total'].widget.attrs.update({'class': 'form-control'})
        self.fields['quantidade_disponivel'].widget.attrs.update({'class': 'form-control'})
