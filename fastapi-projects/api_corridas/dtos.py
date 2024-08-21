from pydantic import BaseModel


# DTO: Data Transfer Object
class RequisicaoCorrida(BaseModel):
  origem: str
  destino: str
  distancia: float