

from loguru import logger

from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorDatabase, AsyncIOMotorCollection

from config import get_config

config = get_config()


class MongoManager:
    client: AsyncIOMotorClient = None
    db: AsyncIOMotorDatabase = None

    async def connect_to_database(self, path: str):
        logger.info("Connecting to MongoDB.")
        self.client = AsyncIOMotorClient(
            path,
            maxPoolSize=10,
            minPoolSize=10)
        self.db: AsyncIOMotorDatabase = self.client.main_db
        logger.info("Connected to MongoDB.")

    async def close_database_connection(self):
        logger.info("Closing connection with MongoDB.")
        self.client.close()
        logger.info("Closed connection with MongoDB.")


db = MongoManager()

async def get_database() -> AsyncIOMotorCollection:
    return db.db[config.app_name]
