from fastapi import APIRouter, status, HTTPException
from dtos import RequisicaoCorrida
from models import Corrida
from utils import calcular_valor
from ulid import ULID


router = APIRouter()

corridas = [
  Corrida(
    id=str(ULID()),
    origem='IFPI THE Central', 
    destino='Riverside', 
    distancia=7, 
    valor=calcular_valor(7)),
]

def get_corrida_by_id(id: str):
  for corrida in corridas:
    if corrida.id == id:
      return corrida
  
  return None

@router.get('/', response_model=list[Corrida])
def corrida_list(estado: str | None = None):

  if estado:
    # significa que é para filtrar
    corridas_filtradas = []
    for corrida in corridas:
      if corrida.estado == estado:
        corridas_filtradas.append(corrida)
    return corridas_filtradas

  return corridas


@router.post('/', 
          response_model=Corrida, 
          status_code=status.HTTP_201_CREATED)
def corrida_create(requisicao: RequisicaoCorrida):
  nova_corrida = Corrida(id=str(ULID()),
                        origem=requisicao.origem,
                         destino=requisicao.destino,
                         distancia=requisicao.distancia, 
                         valor=calcular_valor(requisicao.distancia))
  corridas.append(nova_corrida)
  return nova_corrida

@router.put('/{id}/start')
def corrida_start(id: str):
  corrida_localizada = get_corrida_by_id(id)

  if not corrida_localizada:
    raise HTTPException(
      status_code=status.HTTP_404_NOT_FOUND, 
      detail='Corrida não localizada!')
  
  if not corrida_localizada.estado == 'requisitada':
    raise HTTPException(
      status_code=status.HTTP_400_BAD_REQUEST, 
      detail='Não é possível iniciar essa corrida!')
  
  corrida_localizada.estado = 'em-andamento'

  return corrida_localizada

@router.put('/{id}/finish')
def corrida_start(id: str):
  corrida_localizada = get_corrida_by_id(id)

  if not corrida_localizada:
    raise HTTPException(
      status_code=status.HTTP_404_NOT_FOUND, 
      detail='Corrida não localizada!')
  
  if not corrida_localizada.estado == 'em-andamento':
    raise HTTPException(
      status_code=status.HTTP_400_BAD_REQUEST, 
      detail='Não é possível finalizar essa corrida!')
  
  corrida_localizada.estado = 'finalizada'

  return corrida_localizada


@router.put('/{id}/cancel')
def corrida_start(id: str):
  corrida_localizada = get_corrida_by_id(id)

  if not corrida_localizada:
    raise HTTPException(
      status_code=status.HTTP_404_NOT_FOUND, 
      detail='Corrida não localizada!')
  
  if not corrida_localizada.estado == 'requisitada':
    raise HTTPException(
      status_code=status.HTTP_400_BAD_REQUEST, 
      detail='Não é possível cancelar esta corrida!')
  
  corrida_localizada.estado = 'cancelada'

  return corrida_localizada


