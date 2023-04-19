from database import db

from users.models import UserCreationModel


async def create_user_service(user: UserCreationModel):
    result = await db.insert_one(user.dict())
    return result.inserted_id
