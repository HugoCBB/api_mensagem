from django.urls import path, include
from rest_framework import routers
from .views import ClienteViewset, MensagemViewset

router = routers.DefaultRouter()
router.register('cliente',ClienteViewset,basename='Cliente'),
router.register('mensagem',MensagemViewset,basename='Mensagem'),

urlpatterns = [
    path('',include(router.urls))
]
