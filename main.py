from fastapi import FastAPI
from app.db import init_db
from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()
    yield

app = FastAPI(title="Task Tracker")

@app.get("/")
def read_root():
    return {"message": "Welcome to Trackle"}

