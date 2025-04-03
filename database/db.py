from motor.motor_asyncio import AsyncIOMotorClient
from beanie import init_beanie
from models.user import User 
from models.profile import Profile
from models.token import Token  

MONGO_URI = "mongodb://localhost:27017"  
DB_NAME = "evolution"

client = AsyncIOMotorClient(MONGO_URI)
database = client[DB_NAME]

async def init_db():
    await init_beanie(database=database, document_models=[User, Profile, Token])  
    print("✅ Base de datos inicializada correctamente.")
