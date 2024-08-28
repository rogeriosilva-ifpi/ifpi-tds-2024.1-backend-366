from fastapi import FastAPI

from corridas_controllers import router
from database import sync_database, get_engine

app = FastAPI()

# Atualizar tabelas
sync_database(get_engine())

app.include_router(router, prefix='/api/rides')

