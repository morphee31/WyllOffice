from fastapi import FastAPI

import uvicorn

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
    if config.env == "prod":
        DB_PATH = f"mongodb://{config.mongo_user}:{config.mongo_password}@{config.mongo_host}:{config.mongo_port}"
    else:
        DB_PATH = f"mongodb://{config.mongo_host}:{config.mongo_port}"
    await db.connect_to_database(path=DB_PATH)


@app.on_event("shutdown")
async def shutdown():
    await db.close_database_connection()


@app.get(
    path="/"
)
async def home():
    return "Welcome on WOOP"

if __name__== "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5000)