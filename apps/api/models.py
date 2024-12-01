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
    

    def __str__(self):
        return self.mensagem
    
class EnviarMensagem(models.Model):

    STATUS = [
        ('success', 'Sucesso'),
        ('error', 'Erro')
    ]
    data = models.DateField(auto_now_add=True)
    mensagem = models.ForeignKey(Mensagem, on_delete=models.CASCADE)
    usuario = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=STATUS, default='success')
    resposta = models.TextField(blank=True, null=True)