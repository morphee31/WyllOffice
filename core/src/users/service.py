from database import get_database

from fastapi import Depends

from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorDatabase, AsyncIOMotorCollection

from users.models import CreateUserModel, ReadUserModel


async def create_user_service(user: CreateUserModel):
    woop_db = await get_database()
    result = await woop_db.insert_one(user.dict())
    return result.inserted_id



async def get_user_service(user: ReadUserModel):
    result = await db.find_one(user.dict(exclude_unset=True), {"_id": -1})
    return result


async def update_user_service():
    pass