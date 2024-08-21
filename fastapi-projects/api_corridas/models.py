from pydantic import BaseModel

class Corrida(BaseModel):
  id: str | None
  origem: str
  destino: str
  distancia: float
  valor: float # subst por um método
  estado: str = 'requisitada'


