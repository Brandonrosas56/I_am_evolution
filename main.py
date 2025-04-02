from fastapi import FastAPI
from routes.user import router as user_router
from routes.profile import router as profile_router
from routes.auth import router as auth_router
from database.db import init_db
from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_db()  # Llama a la función que inicializa la BD
    yield

app = FastAPI(lifespan=lifespan)  # Garantiza que la BD se inicializa antes de recibir solicitudes

@app.get("/")
def read_root():
    return {"message": "Hello, World!"}

app.include_router(user_router, prefix="/register", tags=["user"])

app.include_router(profile_router, prefix="/profile-user", tags=["profile"])

app.include_router(auth_router, prefix="/auth", tags=["auth"])