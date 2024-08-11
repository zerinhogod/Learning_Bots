from motor.motor_asyncio import AsyncIOMotorClient

from config import MONGO_DB_URI

from ..logging import LOGGER

LOGGER(__name__).info("Conectando-se ao seu MongoDB...")
try:
    _mongo_async_ = AsyncIOMotorClient(MONGO_DB_URI)
    mongodb = _mongo_async_.Anon
    LOGGER(__name__).info("Conectado ao seu MongoDB.")
except:
    LOGGER(__name__).error("Falha ao conectar-se ao seu MongoDB.")
    exit()
