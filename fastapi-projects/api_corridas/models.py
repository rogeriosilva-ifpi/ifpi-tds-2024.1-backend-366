# from pydantic import BaseModel
from sqlalchemy import table
from sqlmodel import SQLModel, Field

# class Corrida(BaseModel):
class Corrida(SQLModel, table=True):
  id: int | None = Field(primary_key=True, default=None)
  origem: str
  destino: str
  distancia: float
  valor: float # subst por um método
  estado: str = 'requisitada'

  def start(self):
    if not self.estado == 'requisitada':
      raise Exception()
    
    self.estado = 'em-andamento'
  
  def finish(self):
    self.estado = 'finalizada'

  def cancel(self):
    self.estado = 'cancelada'


