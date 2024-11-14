from rest_framework import serializers
from . models import Cliente, Mensagem

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'

class MensagemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mensagem
        fields = '__all__'