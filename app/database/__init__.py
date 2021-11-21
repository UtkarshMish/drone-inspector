

from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient
from app.config import DB_NAME, HOST_IP, DB_PORT, MONGO_URI
from .Drones import Drones
from .DroneTypes import DroneTypes
from .Pilots import Pilots


async def init_DB():
    client = AsyncIOMotorClient(
        f"mongodb+srv://recipe_project://{HOST_IP}:{DB_PORT}" if not MONGO_URI else MONGO_URI
    )
    await init_beanie(database=client[DB_NAME], document_models=[Drones, DroneTypes, Pilots])
