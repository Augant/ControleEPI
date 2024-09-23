from django.db import models

class Usuario(models.Model):
    nome_usuario = models.CharField(max_length=100)
    cpf = models.CharField(max_length=11, unique=True)
    email = models.EmailField()
    senha = models.CharField(max_length=128)
    endereco = models.TextField()
    tipo_usuario = models.IntegerField(default=2)  # 1 para admin, 2 para usuário normal

    def __str__(self):
        return self.nome_usuario