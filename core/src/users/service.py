from database import get_database

from users.models import CreateUserModel, ReadUserModel, UpdateUserModel

from pymongo import ReturnDocument


async def list_users_service():
    woop_db = await get_database()
    results = list()
    async for user in woop_db.find({"disabled": {"$ne": True}}, {"_id": False, "planning": False}):
        results.append(user)
    return results


async def create_user_service(user: CreateUserModel):
    woop_db = await get_database()
    result = await woop_db.insert_one(user.dict())
    return {
        "id": result.inserted_id,
        "acknowledged": result.acknowledged
    }


async def get_user_service(user: ReadUserModel):
    woop_db = await get_database()
    result = await woop.db.find_one(user.dict(exclude_unset=True), {"_id": -1})
    return result


async def update_user_service(user_id:str, user: UpdateUserModel):
    woop_db = await get_database()
    result_update = await woop_db.find_one_and_update(
        filter={"user_id": user_id},
        update={"$set" : user.dict(
            exclude_unset=True,
            exclude_none=True,
            ),
        },
        projection={"_id": False},
        return_document=ReturnDocument.AFTER
    )
    return result_update
