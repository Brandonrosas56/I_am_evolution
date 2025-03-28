from fastapi import FastAPI
from routes.register import register_router 

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, World!"}

app.include_router(register_router, prefix="/register", tags=["register"])