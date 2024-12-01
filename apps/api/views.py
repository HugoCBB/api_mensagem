from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from .serializers import ClienteSerializer, MensagemSerializer, EnviarMensagemSerializer

from .models import Cliente, Mensagem, EnviarMensagem

from .bot import BOT_MENSAGEM

# Create your views here.

class ClienteViewset(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

class MensagemViewset(viewsets.ModelViewSet):
    queryset = Mensagem.objects.all()
    serializer_class = MensagemSerializer

class EnviarMensagemViewset(viewsets.ModelViewSet):
    queryset = EnviarMensagem.objects.all()
    serializer_class = EnviarMensagemSerializer


    def perform_create(self, serializer):
        instance = serializer.save(status='Pending')

        try:
            # Inicializar o bot para enviar a mensagem
            resposta = BOT_MENSAGEM()

            # Acessa o site (exemplo de inicialização do bot)
            resposta.AcessarSite()

            # Envia a mensagem
            sucesso = resposta.EnviarMensagem(instance.usuario.telefone, instance.mensagem.mensagem)

            # Se a mensagem for enviada com sucesso, atualiza o status
            if sucesso:
                instance.status = 'success'
            else:
                instance.status = 'error'
                instance.resposta = "Falha no envio"

        except Exception as e:
            # Caso ocorra um erro durante o envio
            instance.status = 'error'
            instance.resposta = str(e)

        # Salva as alterações feitas no modelo
        instance.save()

        