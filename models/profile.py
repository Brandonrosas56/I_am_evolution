from datetime import datetime
from typing import Optional
from beanie import Document  # Importa Document en lugar de BaseModel

class Profile(Document):  # Usa Document en lugar de BaseModel
    weight: float  
    stature: float  
    age: Optional[int] = None  
    disease: str  
    medicine: str  
    goal: Optional[str] = None  
    body_type: bool = False  
    sleeping_time: Optional[datetime] = None  
    preferred_diet: Optional[int] = None  
    habit: bool = True  

    class Settings:
        collection = "profile"  # Nombre de la colección en MongoDB
