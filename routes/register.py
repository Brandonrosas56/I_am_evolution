from fastapi import APIRouter
from pydantic import BaseModel

register_router = APIRouter()

class User(BaseModel):
    name: str
    age: int

@register_router.post("/create-user")
def create_user(user: User):
    return {"message": f"User {user.name} created", "age": user.age}
