from django.shortcuts import render
from django.http import HttpResponse

def saudacao(request):
  nome = 'Rogerio'
  response = HttpResponse(f'Olá {nome}, sucesso!')
  return response
