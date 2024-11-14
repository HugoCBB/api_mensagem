from django.db import models

# Create your models here.

class Cliente(models.Model):
    data = models.DateField(auto_now_add=True)
    nome = models.CharField(max_length=50)
    telefone = models.CharField(max_length=15, blank=False, null=False,)
    cpf = models.IntegerField(blank=True, null=True)

    def __str__(self) -> str:
        return self.nome
    
class Mensagem(models.Model):
    data = models.DateField(auto_now_add=True)
    mensagem = models.CharField(max_length=1000)
