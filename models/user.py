from beanie import Document
from typing import Optional
from datetime import datetime

class User(Document):
    name: str
    lastname: str
    phone: Optional[int] = None
    email: str
    password: str
    token: Optional[str] = None
    subscription: Optional[bool] = False
    end_subscription: Optional[datetime] = None
    identification: Optional[int] = None
    user_status: Optional[bool] = True
    date_of_registration: Optional[datetime] = datetime.utcnow()
    last_connection: Optional[datetime] = None

    class Settings:
        collection = "users"
