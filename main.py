from fastapi import FastAPI
from routes.user import router as user_router

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, World!"}

app.include_router(user_router, prefix="/register", tags=["user"])