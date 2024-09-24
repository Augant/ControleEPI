from django import forms
from .models import Emprestimo
from app_usuarios.models import Usuario
from app_cadastroEPI.models import Epi

class EmprestimoForm(forms.ModelForm):
    class Meta:
        model = Emprestimo
        fields = ['usuario', 'epi', 'quantidade', 'data_devolucao']  # Adicionando 'quantidade'
        labels = {
            'usuario': 'Funcionário',
            'epi': 'EPI',
            'quantidade': 'Quantidade Emprestada',
            'data_devolucao': 'Data de Devolução',
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['usuario'].widget.attrs.update({'class': 'form-control'})
        self.fields['epi'].widget.attrs.update({'class': 'form-control'})
        self.fields['quantidade'].widget.attrs.update({'class': 'form-control'})  # Estilo para quantidade
        self.fields['data_devolucao'].widget.attrs.update({'class': 'form-control', 'type': 'date'})
