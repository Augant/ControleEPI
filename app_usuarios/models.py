from django.db import models

class Usuario(models.Model):
    TIPOS_USUARIO = [
        ('admin', 'Admin'),
        ('colaborador', 'Colaborador'),
        ('sem_acesso', 'Sem acesso'),
    ]
    
    nome_usuario = models.CharField(max_length=100)
    cpf = models.CharField(max_length=11, unique=True)
    email = models.EmailField()
    senha = models.CharField(max_length=128)
    endereco = models.CharField(max_length=150)  # Mantendo o tamanho de 150
    tipo_usuario = models.CharField(max_length=15, choices=TIPOS_USUARIO, default='colaborador')  # Alterado para CharField com choices

    def __str__(self):
        return self.nome_usuario