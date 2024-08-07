from unittest.mock import Base
from fastapi import FastAPI
from pydantic import BaseModel
from ulid import ULID

app = FastAPI()

esportes = [
  {
    'id': str(ULID()),
    'nome': 'Vôlei',
    'tipo': 'Feminino',
    'coletivo': True
  }, 
  {
    'id': str(ULID()),
    'nome': 'Skate',
    'tipo': 'Masculino',
    'coletivo': False
  }, 
]

class Esporte(BaseModel):
  nome: str
  tipo: str
  coletivo: bool


@app.get("/esportes")
def esportes_lista():
  return esportes

@app.get('/esportes/{id}')
def esporte_detalhes(id: str):
  # buscar na lista e retornar
  for esporte in esportes:
    if esporte['id'] == id:
      return esporte
  
  return {}

@app.delete('/esportes/{id}')
def esporte_remover(id: str):
  for e in esportes:
    if e['id'] == id:
      esportes.remove(e)
      return {}
  
  return {}

@app.post('/esportes')
def esporte_criar(esporte: Esporte):
  esportes.append({
    'id': str(ULID()),
    'nome': esporte.nome,
    'tipo': esporte.tipo,
    'coletivo': esporte.coletivo
  })

  return {}

@app.put('/esportes/{id}')
def esporte_atualizar():
  pass


@app.get("/home")
def home():
  return "Bem vindos aos Jogos de 2024"