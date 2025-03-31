from fastapi import APIRouter, HTTPException
from models.user import User

router = APIRouter()

# Crear usuario
@router.post("/")
async def create_user(user: User):
    await user.insert()
    return user
