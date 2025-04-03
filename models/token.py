from beanie import Document
from datetime import datetime
from pydantic import Field
from typing import Optional
from bson import ObjectId  # Importamos ObjectId

class Token(Document):
    user_id: str = Field(...)  # Guardamos el ID del usuario como string
    token: str
    created_at: datetime = Field(default_factory=datetime.utcnow)
    expires_at: Optional[datetime] = None

    class Settings:
        name = "Token"  # Nombre de la colección en la base de datos
