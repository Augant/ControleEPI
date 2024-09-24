from django.db import models
from app_usuarios.models import Usuario  # Importa o modelo Usuario
from app_cadastroEPI.models import Epi    # Importa o modelo Epi

class Emprestimo(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    epi = models.ForeignKey(Epi, on_delete=models.CASCADE)
    data_emprestimo = models.DateField(auto_now_add=True)
    data_devolucao = models.DateField(null=True, blank=True)
    
    def __str__(self):
        return f'{self.usuario.nome_usuario} - {self.epi.nome_epi}'