from database import get_database

from users.models import CreateUserModel, ReadUserModel


async def list_users_service():
    woop_db = await get_database()
    result = await woop_db.find({"disabled": {"$ne": True}}, {"_id": -1})
    return result


async def create_user_service(user: CreateUserModel):
    woop_db = await get_database()
    result = await woop_db.insert_one(user.dict())
    return {
        "id": result.inserted_id,
        "acknowledged": result.acknowledged
    }


async def get_user_service(user: ReadUserModel):
    result = await db.find_one(user.dict(exclude_unset=True), {"_id": -1})
    return result


async def update_user_service():
    pass
