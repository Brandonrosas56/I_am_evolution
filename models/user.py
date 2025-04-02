from beanie import Document
from typing import Optional
from datetime import datetime
from pydantic import root_validator
import bcrypt

class User(Document):
    name: str
    lastname: str
    phone: Optional[int] = None
    email: str
    password: str  # Esta se va a encriptar automáticamente
    token: Optional[str] = None
    subscription: Optional[bool] = False
    end_subscription: Optional[datetime] = None
    identification: Optional[int] = None
    user_status: Optional[bool] = True
    date_of_registration: Optional[datetime] = datetime.utcnow()
    last_connection: Optional[datetime] = None

    class Config:
        collection = "users"

    @root_validator(pre=True)
    def hash_password(cls, values):
        password = values.get('password')
        if password and not password.startswith('$2b$'):  # Esto evita re-encriptar si ya viene hasheada
            salt = bcrypt.gensalt()
            hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
            values['password'] = hashed.decode('utf-8')
        return values
