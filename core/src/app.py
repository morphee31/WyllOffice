from fastapi import FastAPI

from config import get_config
from database import db
from users.router import user_router

from loguru import logger

app = FastAPI()
app.include_router(user_router)


@app.on_event("startup")
async def startup():
    config = get_config()
    logger.info(f"Statup {config.app_name}")
    DB_PATH = f"mongodb://{config.mongo_user}:{config.mongo_password}@{config.mongo_host}:{config.mongo_port}"
    await db.connect_to_database(path=DB_PATH)


@app.on_event("shutdown")
async def shutdown():
    await db.close_database_connection()
