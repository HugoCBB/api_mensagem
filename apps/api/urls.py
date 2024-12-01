from django.urls import path, include
from rest_framework import routers
from .views import ClienteViewset, MensagemViewset, EnviarMensagemViewset

router = routers.DefaultRouter()
router.register('cliente',ClienteViewset,basename='Cliente'),
router.register('mensagem',MensagemViewset,basename='Mensagem'),
router.register('enviar-mensagem',EnviarMensagemViewset,basename='EnviarMensagem'),

urlpatterns = [
    path('api/',include(router.urls))
]
