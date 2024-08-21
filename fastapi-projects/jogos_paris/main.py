from unittest.mock import Base
from fastapi import FastAPI, HTTPException, Response
from pydantic import BaseModel
from ulid import ulid

app = FastAPI()


class Esporte(BaseModel):
    id: str | None
    nome: str
    tipo: str
    coletivo: bool


esportes: list[Esporte] = [
    Esporte(id=str(ulid()), nome='Futebol', tipo='Feminino', coletivo=True),
    Esporte(id=str(ulid()), nome='Vôlei de Praia',
            tipo='Feminino', coletivo=True),
]


@app.get("/esportes")
def esportes_lista() -> list[Esporte]:
    return esportes


@app.get('/esportes/{id}')
def esporte_detalhes(id: str) -> Esporte:
    # buscar na lista e retornar
    for esporte in esportes:
        if esporte.id == id:
            return esporte

    raise HTTPException(status_code=404, detail='Esporte não localizado!')


@app.delete('/esportes/{id}')
def esporte_remover(id: str):
    for e in esportes:
        if e.id == id:
            esportes.remove(e)
            return Response(status_code=204)

    raise HTTPException(status_code=404, detail='Esporte não localizado!')


@app.post('/esportes')
def esporte_criar(esporte: Esporte) -> Esporte:
    esporte = Esporte(id=str(ulid()), nome=esporte.nome,
                      tipo=esporte.tipo, coletivo=esporte.coletivo)

    esportes.append(esporte)

    return Response(status_code=201, content=esporte)


@app.put('/esportes/{id}')
def esporte_atualizar(id: str, esporte: Esporte):
    for e in esportes:
        if id == e.id:
            e.nome = esporte.nome
            e.tipo = esporte.tipo
            e.coletivo = esporte.coletivo
            return Response(content=e)

    raise HTTPException(status_code=404, detail='Esporte não localizado!')


@app.get("/home")
def home():
    return "Bem vindos aos Jogos de 2024"
