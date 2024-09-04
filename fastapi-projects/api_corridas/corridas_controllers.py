from fastapi import APIRouter, status, HTTPException
from dtos import RequisicaoCorrida
from models import Corrida
from utils import calcular_valor
from ulid import ULID
from sqlmodel import Session, select
from database import get_engine
from corridas_service import CorridaService


router = APIRouter()

# Corrida Service
corrida_service = CorridaService()


@router.get("/{id}")
def corrida_detail(id: int):
  return corrida_service.get_corrida_by_id(id)


@router.get('/', response_model=list[Corrida])
def corrida_list(estado: str | None = None):
  return corrida_service.get_all_corridas(estado)


@router.post('/', 
          response_model=Corrida, 
          status_code=status.HTTP_201_CREATED)
def corrida_create(requisicao: RequisicaoCorrida):
  nova_corrida = Corrida(origem=requisicao.origem,
                         destino=requisicao.destino,
                         distancia=requisicao.distancia, 
                         valor=calcular_valor(requisicao.distancia))

  return corrida_service.save_corrida(nova_corrida)


@router.put('/{id}/start')
def corrida_start(id: str):
  corrida_localizada = corrida_service.get_corrida_by_id(id)

  if not corrida_localizada:
    raise HTTPException(
      status_code=status.HTTP_404_NOT_FOUND, 
      detail='Corrida não localizada!')
    
  try:
    corrida_localizada.start()
  except:
    raise HTTPException(
      status_code=status.HTTP_400_BAD_REQUEST, 
      detail='Não é possível iniciar essa corrida!')

  return corrida_service.save_corrida(corrida_localizada)


@router.put('/{id}/finish')
def corrida_finish(id: str):
  corrida_localizada = corrida_service.get_corrida_by_id(id)

  if not corrida_localizada:
    raise HTTPException(
      status_code=status.HTTP_404_NOT_FOUND, 
      detail='Corrida não localizada!')
  
  if not corrida_localizada.estado == 'em-andamento':
    raise HTTPException(
      status_code=status.HTTP_400_BAD_REQUEST, 
      detail='Não é possível finalizar essa corrida!')
  
  corrida_localizada.estado = 'finalizada'

  return corrida_service.save_corrida(corrida_localizada)


@router.put('/{id}/cancel')
def corrida_cancel(id: str):
  corrida_localizada = corrida_service.get_corrida_by_id(id)

  if not corrida_localizada:
    raise HTTPException(
      status_code=status.HTTP_404_NOT_FOUND, 
      detail='Corrida não localizada!')
  
  if not corrida_localizada.estado == 'requisitada':
    raise HTTPException(
      status_code=status.HTTP_400_BAD_REQUEST, 
      detail='Não é possível cancelar esta corrida!')
  
  corrida_localizada.estado = 'cancelada'

  return corrida_service.save_corrida(corrida_localizada)

