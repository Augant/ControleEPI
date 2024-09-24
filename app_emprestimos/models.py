from django.db import models
from app_usuarios.models import Usuario
from app_cadastroEPI.models import Epi

class Emprestimo(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    epi = models.ForeignKey(Epi, on_delete=models.CASCADE)
    data_emprestimo = models.DateField(auto_now_add=True)
    data_devolucao = models.DateField(null=True, blank=True)
    quantidade = models.IntegerField()  # Campo para a quantidade emprestada

    def __str__(self):
        return f'{self.usuario.nome_usuario} - {self.epi.nome_epi}'
