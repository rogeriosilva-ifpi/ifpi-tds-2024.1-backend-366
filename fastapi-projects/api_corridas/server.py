from fastapi import FastAPI

from corridas_controllers import router

app = FastAPI()

app.include_router(router, prefix='/api/rides')

