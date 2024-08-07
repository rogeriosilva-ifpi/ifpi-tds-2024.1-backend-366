from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Dados(BaseModel):
    nome: str


@app.post('/saudacao')
def saudacao(dados: Dados):
    return {'caracteres': len(dados.nome)}


@app.get('/home')
def home():
    return 'Hello FastAPI'


@app.get('/hello')
def index():
    return {'nome': 'Rogério da Silva'}
