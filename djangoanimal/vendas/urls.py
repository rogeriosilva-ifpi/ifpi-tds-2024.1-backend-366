from django.urls import path
from vendas.views import listar_pedidos

urlpatterns = [
    path('pedidos', listar_pedidos),
]