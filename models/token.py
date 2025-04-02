from beanie import Document
from datetime import datetime
from typing import Optional

class Token(Document):
    user_id: str  # ID del usuario al que pertenece el token
    token: str  # Token generado
    created_at: datetime = datetime.utcnow()
    expires_at: Optional[datetime] = None  # Fecha de expiración

    class Settings:
        collection = "tokens"
