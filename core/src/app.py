from fastapi import FastAPI

from users.router import user_router

from database import db



app = FastAPI()
app.include_router(user_router)

@app.on_event("startup")
async def startup():
    config = get_config()
    DB_PATH = f"mongodb://{MONGODB_USER}:{MONGODB_PASSWORD}@{MONGO_HOST}:{MONGO_PORT}"
    await db.connect_to_database(path=config.db_path)


@app.on_event("shutdown")
async def shutdown():
    await db.close_database_connection()
