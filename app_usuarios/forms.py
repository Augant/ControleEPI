from django import forms
from .models import Usuario

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['nome_usuario', 'cpf', 'email', 'senha', 'endereco', 'tipo_usuario']
        labels = {
            'nome_usuario': 'Nome do Usuário',
            'cpf': 'CPF',
            'email': 'Email',
            'senha': 'Senha',
            'endereco': 'Endereço',
            'tipo_usuario': 'Tipo de Usuário',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['nome_usuario'].widget.attrs.update({'class': 'form-control'})
        self.fields['cpf'].widget.attrs.update({'class': 'form-control'})
        self.fields['email'].widget.attrs.update({'class': 'form-control'})
        self.fields['senha'].widget.attrs.update({'class': 'form-control', 'type': 'password'})
        self.fields['endereco'].widget.attrs.update({'class': 'form-control'})
        self.fields['tipo_usuario'].widget.attrs.update({'class': 'form-control'})
