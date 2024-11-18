from django.shortcuts import render
from apps.api.models import Cliente

# Create your views here.

def home(request):
    clientes = Cliente.objects.all()
    return render(request, 'paginas/home.html',{'clientes':clientes})