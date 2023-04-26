from database import get_database

from users.models import CreateUserModel, ReadUserModel, UpdateUserModel

from pymongo import ReturnDocument

from users.schemas import Planning

from datetime import datetime


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


async def get_user_service(user_id: str):
    woop_db = await get_database()
    result = await woop_db.find_one(
        filter={"user_id":user_id}, 
        projection={"_id": False}
        )
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


async def get_users_by_date(date:datetime):
    woop_db = await get_database()
    pipeline = [
        {
        '$project': {
            'user_id': "$user_id",
            "date": {
                "$in": [date, "$planning.day"]
            }
            }}
        ]
    results = await woop_db.aggregate(pipeline)
    return results

async def add_date_to_user(user_id:str, date: Planning):
    woop_db = await get_database()
    result_update = await woop_db.find_one_and_update(
        filter={"user_id": user_id},
        update={"$push" : {
            "planning": date.dict()
        }
        },
        projection={"_id": False},
        return_document=ReturnDocument.AFTER
    )
    return result_update


async def remove_date_to_user(user_id:str, date: datetime):
    woop_db = await get_database()
    result_update = await woop_db.find_one(
        filter={"user_id": user_id},
        projection={
            "_id": False
        })
    for _date in result_update["planning"]:
        if _date["day"] == date:
            # find_result["planning"].remove(_date)
            result_update = await woop_db.find_one_and_update(
                filter={"user_id": user_id},
                update={"$pull" : {
                    "planning": _date
                }
                },
                projection={"_id": False},
                return_document=ReturnDocument.AFTER
            )
    return result_update


