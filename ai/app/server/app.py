from fastapi import FastAPI

from server.routes.recipe import router as AIRouter

app = FastAPI()

app.include_router(AIRouter, tags=["AI"], prefix="/ai")