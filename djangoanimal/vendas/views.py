from django.shortcuts import render
from django.http import HttpResponse

def listar_pedidos(request):
  return HttpResponse(content='Meus Pedidos')
