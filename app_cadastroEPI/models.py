from django.db import models

class Epi(models.Model):
    nome_epi = models.CharField(max_length=100)
    descricao_epi = models.TextField()
    quantidade_total = models.IntegerField()
    quantidade_disponivel = models.IntegerField()

    def __str__(self):
        return self.nome_epi