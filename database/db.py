from motor.motor_asyncio import AsyncIOMotorClient
import os

# URL de conexión a MongoDB
MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017")

# Nombre de la base de datos
DATABASE_NAME = "Evolution"

class Database:
    client: AsyncIOMotorClient = None
    db = None

db = Database()

async def connect_db():
    """Conectar a la base de datos."""
    db.client = AsyncIOMotorClient(MONGO_URI)
    db.db = db.client[DATABASE_NAME]
    print("✅ Conectado a MongoDB")

async def close_db():
    """Cerrar la conexión con la base de datos."""
    if db.client:
        db.client.close()
        print("❌ Conexión con MongoDB cerrada")
