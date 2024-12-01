from rest_framework import serializers
from . models import Cliente, Mensagem, EnviarMensagem
from .bot import BOT_MENSAGEM
class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'

class MensagemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mensagem
        fields = '__all__'

class EnviarMensagemSerializer(serializers.ModelSerializer):
    class Meta:
        model = EnviarMensagem
        fields = '__all__'