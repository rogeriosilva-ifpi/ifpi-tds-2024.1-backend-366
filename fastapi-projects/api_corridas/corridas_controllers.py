from fastapi import APIRouter, status, HTTPException
from dtos import RequisicaoCorrida
from models import Corrida
from utils import calcular_valor
from ulid import ULID
from sqlmodel import Session, select
from database import get_engine


router = APIRouter()

corridas = [
  Corrida(
    id=str(ULID()),
    origem='IFPI THE Central', 
    destino='Timon', 
    distancia=7, 
    valor=calcular_valor(7)),
]

def get_corrida_by_id(id: int):
  session = Session(get_engine())
  sttm = select(Corrida).where(Corrida.id==id)
  return session.exec(sttm).one_or_none()

@router.get('/', response_model=list[Corrida])
def corrida_list(estado: str | None = None):
  with Session(get_engine()) as session:
    sttm = select(Corrida)
    
    if estado:
      sttm = sttm.where(Corrida.estado==estado)

    return session.exec(sttm).all()


@router.post('/', 
          response_model=Corrida, 
          status_code=status.HTTP_201_CREATED)
def corrida_create(requisicao: RequisicaoCorrida):
  nova_corrida = Corrida(origem=requisicao.origem,
                         destino=requisicao.destino,
                         distancia=requisicao.distancia, 
                         valor=calcular_valor(requisicao.distancia))
  # Mandar o BD
  with Session(get_engine()) as session:
    session.add(nova_corrida)
    session.commit()
    session.refresh(nova_corrida)

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

  session = Session(get_engine())
  session.commit()
  session.refresh(corrida_localizada)

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


