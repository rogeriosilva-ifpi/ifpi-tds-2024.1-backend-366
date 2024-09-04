from sqlmodel import Session, select
from database import get_engine
from models import Corrida

class CorridaService():

  def __init__(self):
    engine = get_engine()
    self.session = Session(engine)
  
  def get_corrida_by_id(self, id: int):
    sttm = select(Corrida).where(Corrida.id==id)
    return self.session.exec(sttm).one_or_none()
  
  def get_all_corridas(self, estado: str | None = None):
    sttm = select(Corrida)
    
    if estado:
      sttm = sttm.where(Corrida.estado==estado)

    return self.session.exec(sttm).all()
  
  def save_corrida(self, corrida: Corrida):
    self.session.add(corrida)
    self.session.commit()
    self.session.refresh(corrida)
    return corrida