from database import get_database

from users.models import CreateUserModel, ReadUserModel, UpdateUserModel

from pymongo import ReturnDocument

from users.schemas import Planning
from planning.schemas import PlanningResult


from datetime import datetime


async def get_users_by_date(date:datetime):
    woop_db = await get_database()
    results = list()
    async for user in woop_db.find({ "disabled": {"$ne": True},"planning.day":{ "$all": [date] }}, {"_id": False, "user_id": True, "firstname":True, "lastname": True}):
        results.append(PlanningResult(**user))
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


