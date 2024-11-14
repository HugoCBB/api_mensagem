from django.shortcuts import render
from rest_framework import viewsets
from .serializers import ClienteSerializer, MensagemSerializer

from .models import Cliente, Mensagem

# Create your views here.

class ClienteViewset(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

class MensagemViewset(viewsets.ModelViewSet):
    queryset = Mensagem.objects.all()
    serializer_class = MensagemSerializer
