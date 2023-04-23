from database import db

from users.models import UserCreationModel


async def create_user_service(user: UserCreationModel):
    result = await db.insert_one(user.dict())
    return result.inserted_id



async def get_user_service(user: ReadUserModel):
    result = await db.find_one(user.dict(exclude_unset=True), {"_id": -1})
    return result


async def update_user_service():
    pass