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


