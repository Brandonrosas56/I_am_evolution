from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient
from models.user import User

MONGO_URI = "mongodb://localhost:27017"

async def init_db():
    client = AsyncIOMotorClient(MONGO_URI)
    db = client.Evolution  # Nombre de la base de datos
    await init_beanie(database=db, document_models=[User])
