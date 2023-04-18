from loguru import logger
from typing import List

from bson import ObjectId
from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorDatabase, AsyncIOMotorCollection

from app.db import DatabaseManager
from app.db.models import PostDB, OID


class MongoManager:
    client: AsyncIOMotorClient = None
    db: AsyncIOMotorDatabase = None

    async def connect_to_database(self, path: str):
        logger.info("Connecting to MongoDB.")
        self.client = AsyncIOMotorClient(
            path,
            maxPoolSize=10,
            minPoolSize=10)
        self.db :AsyncIOMotorDatabase = self.client.main_db
        self.db :AsyncIOMotorCollection= db[config.app_name]
        logger.info("Connected to MongoDB.")

    async def close_database_connection(self):
        logger.info("Closing connection with MongoDB.")
        self.client.close()
        logger.info("Closed connection with MongoDB.")


db = MongoManager()
